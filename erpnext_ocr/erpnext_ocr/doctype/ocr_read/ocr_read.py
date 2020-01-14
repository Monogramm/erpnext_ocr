# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and contributors
# Copyright (c) 2019, Monogramm and Contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import re
import time

import frappe
from frappe.model.document import Document

from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import lang_available

import os
import io

from spellchecker import SpellChecker

def get_words_from_text(message):
    '''
    This function return only list of words from text. Example: Cat in gloves,
    catches: no mice ->[cat, in, gloves, catches, no, mice]
    '''
    message = re.sub(r'\W+', " ", message)
    word_list = list(filter(None, message.split()))
    return word_list


def get_spellchecked_text(message, language):
    '''
    :param message: return text with correction:
    Example: Cet in glaves cetches no mice -> Cat in gloves catches no mice
    '''
    lang = frappe.get_doc("OCR Language", language).lang
    spell_checker = SpellChecker(lang)
    only_words = get_words_from_text(message)
    misspelled = spell_checker.unknown(only_words)
    for word in misspelled:
        corrected_word = spell_checker.correction(word)
        message = message.replace(word, corrected_word)
    return message


class OCRRead(Document):
    def read_image(self):
        start_time = time.time()
        text = read_document(self.file_to_read, self.language or 'eng',
                             self.spell_checker)
        delta_time = time.time() - start_time
        self.time_read = str(delta_time)
        self.read_result = text
        self.save()
        return text, delta_time


@frappe.whitelist()
def read_document(path, lang='eng', spellcheck=False, event="ocr_progress_bar"):
    """Call Tesseract OCR to extract the text from a document."""
    from PIL import Image
    import requests
    import tesserocr

    if path is None:
        return None

    if not lang_available(lang):
        frappe.msgprint(
            frappe._("The selected language is not available. Please contact your administrator."),
                        raise_exception=True)

    frappe.publish_realtime(event, {"progress": "0"}, user=frappe.session.user)

    if path.startswith('/assets/'):
        # from public folder
        fullpath = os.path.abspath(path)
    elif path.startswith('/files/'):
        # public file
        fullpath = frappe.get_site_path() + '/public' + path
    elif path.startswith('/private/files/'):
        # private file
        fullpath = frappe.get_site_path() + path
    elif path.startswith('/'):
        # local file (mostly for tests)
        fullpath = os.path.abspath(path)
    else:
        # external link
        fullpath = requests.get(path, stream=True).raw

    ocr = frappe.get_doc("OCR Settings")

    text = " "
    with tesserocr.PyTessBaseAPI(lang=lang) as api:

        if path.endswith('.pdf'):
            from wand.image import Image as wi

            # https://stackoverflow.com/questions/43072050/pyocr-with-tesseract-runs-out-of-memory
            with wi(filename=fullpath, resolution=ocr.pdf_resolution) as pdf:
                pdf_image = pdf.convert('jpeg')
                i = 0
                size = len(pdf_image.sequence) * 3

                for img in pdf_image.sequence:
                    with wi(image=img) as img_page:
                        image_blob = img_page.make_blob('jpeg')
                        frappe.publish_realtime(
                            event, {"progress": [i, size]}, user=frappe.session.user)
                        i += 1

                        recognized_text = " "

                        image = Image.open(io.BytesIO(image_blob))
                        api.SetImage(image)
                        frappe.publish_realtime(
                            event, {"progress": [i, size]}, user=frappe.session.user)
                        i += 1

                        recognized_text = api.GetUTF8Text()
                        text = text + recognized_text
                        frappe.publish_realtime(
                            event, {"progress": [i, size]}, user=frappe.session.user)
                        i += 1

        else:
            image = Image.open(fullpath)
            api.SetImage(image)
            frappe.publish_realtime(
                event, {"progress": [33, 100]}, user=frappe.session.user)

            text = api.GetUTF8Text()
            frappe.publish_realtime(
                event, {"progress": [66, 100]}, user=frappe.session.user)

    if spellcheck:
        text = get_spellchecked_text(text, lang)

    frappe.publish_realtime(
        event, {"progress": [100, 100]}, user=frappe.session.user)

    return text


def force_attach_file_doc(filename, name):
    """Alternative to 'File Upload Disconnected. Please try again.'"""
    file_url = "/private/files/" + filename

    attachment_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "file_url": file_url,
        "attached_to_name": name,
        "attached_to_doctype": "OCR Read",
        "old_parent": "Home/Attachments",
        "folder": "Home/Attachments",
        "is_private": 1
    })
    attachment_doc.insert()

    frappe.db.sql(
        """UPDATE `tabOCR Read` SET file_to_read=%s WHERE name=%s""", (file_url, name))
