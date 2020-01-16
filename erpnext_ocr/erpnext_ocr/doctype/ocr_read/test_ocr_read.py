# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and Contributors
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import time

import frappe
import unittest
import os

from erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read import force_attach_file_doc

# TODO Frappe default test records creation
#def _make_test_records(verbose):
#    from frappe.test_runner import make_test_objects
#
#    docs = [
#        # [file_to_read, language]
#        [os.path.join(os.path.dirname(__file__),
#                      os.path.pardir, os.path.pardir, os.path.pardir,
#                      "tests", "test_data", "sample1.jpg"), "eng"],
#        [os.path.join(os.path.dirname(__file__),
#                      os.path.pardir, os.path.pardir, os.path.pardir,
#                      "tests", "test_data", "Picture_010.png"), "eng"],
#        [os.path.join(os.path.dirname(__file__),
#                      os.path.pardir, os.path.pardir, os.path.pardir,
#                      "tests", "test_data", "sample2.pdf"), "eng"],
#    ]
#
#    test_objects = make_test_objects("OCR Read", [{
#            "doctype": "OCR Read",
#            "file_to_read": file_to_read,
#            "language": language
#        } for file_to_read, language in docs])
#
#    return test_objects


def create_ocr_reads():
    if frappe.flags.test_ocr_reads_created:
        return

    frappe.set_user("Administrator")
    frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read": os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample1.jpg"),
        "language": "eng"
    }).insert()

    frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read": os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "Picture_010.png"),
        "language": "eng"
    }).insert()

    frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read": os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample2.pdf"),
        "language": "eng"
    }).insert()

    frappe.flags.test_ocr_reads_created = True


def delete_ocr_reads():
    if frappe.flags.test_ocr_reads_created:
        frappe.set_user("Administrator")

        for d in frappe.get_all("OCR Read"):
            doc = frappe.get_doc("OCR Read", d.name)
            doc.delete()

        # Delete directly in DB to avoid validation errors
        #frappe.db.sql("""delete from `tabOCR Read`""")

        frappe.flags.test_ocr_reads_created = False


class TestOCRRead(unittest.TestCase):
    def setUp(self):
        create_ocr_reads()

    def tearDown(self):
        delete_ocr_reads()

    def test_ocr_read_image_bg(self):
        frappe.set_user("Administrator")
        doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "sample1.jpg"),
            "language": "eng"
        })

        self.assertEqual(None, doc.read_result)

        worker = doc.read_image_bg()
        # [TODO] Test worker completion before moving on in the tests
        time.sleep(5) # TODO: Will be better if we can understand how realize producer-consumer pattern
        self.assertIsNotNone(worker.ended_at)

        self.assertEqual(None, doc.read_result)

        new_doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "sample1.jpg"),
            "language": "eng"
        })

        self.assertNotEqual(new_doc.read_result, doc.read_result)

        self.assertIn("The quick brown fox", new_doc.read_result)
        self.assertIn("jumped over the 5", new_doc.read_result)
        self.assertIn("lazy dogs!", new_doc.read_result)
        self.assertNotIn("And an elephant!", new_doc.read_result)


    def test_ocr_read_image_bg_pdf(self):
        frappe.set_user("Administrator")
        doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "sample2.pdf"),
            "language": "eng"
        })

        self.assertEqual(None, doc.read_result)

        worker = doc.read_image_bg()
        # [TODO] Test worker completion before moving on in the tests
        time.sleep(5)  # TODO: Will be better if we can understand how realize producer-consumer pattern
        self.assertIsNotNone(worker.ended_at)

        self.assertEqual(None, doc.read_result)

        new_doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "sample1.jpg"),
            "language": "eng"
        })

        # FIXME values are not equal on Alpine ??!
        #self.maxDiff = None
        #self.assertEqual(new_doc.read_result, doc.read_result)

        self.assertIn("Python Basics", new_doc.read_result)
        self.assertNotIn("Java", new_doc.read_result)


    def test_ocr_read_image(self):
        frappe.set_user("Administrator")
        doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "sample1.jpg"),
            "language": "eng"
        })

        recognized_text = doc.read_image()
        self.assertEqual(recognized_text, doc.read_result)

        self.assertIn("The quick brown fox", recognized_text)
        self.assertIn("jumped over the 5", recognized_text)
        self.assertIn("lazy dogs!", recognized_text)
        self.assertNotIn("And an elephant!", recognized_text)


    def test_ocr_read_pdf(self):
        frappe.set_user("Administrator")
        doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "sample2.pdf"),
            "language": "eng"
        })

        recognized_text = doc.read_image()

        # FIXME values are not equal on Alpine ??!
        #self.maxDiff = None
        #self.assertEqual(recognized_text, doc.read_result)

        self.assertIn("Python Basics", recognized_text)
        self.assertNotIn("Java", recognized_text)


    def test_force_attach_file_doc(self):
        doc = frappe.get_doc({
            "doctype": "OCR Read",
            "file_to_read": os.path.join(os.path.dirname(__file__),
                                        os.path.pardir, os.path.pardir, os.path.pardir,
                                        "tests", "test_data", "Picture_010.png"),
            "language": "eng"
        })

        force_attach_file_doc('test.tif', doc.name)

        forced_doc = frappe.get_doc({
            "doctype": "OCR Read",
            #"name": doc.name,
            "file_to_read": "/private/files/test.tif",
            "language": "eng"
        })
        self.assertIsNotNone(forced_doc)
        self.assertEqual(forced_doc.name, doc.name)
        self.assertEqual('/private/files/test.tif', forced_doc.file_to_read)


    def test_ocr_read_list(self):
        # frappe.set_user("test1@example.com")
        frappe.set_user("Administrator")
        res = frappe.get_list("OCR Read", filters=[
                              ["OCR Read", "file_to_read", "like", "%sample%"]], fields=["name", "file_to_read"])
        self.assertEqual(len(res), 2)
        files_to_read = [r.file_to_read for r in res]
        self.assertTrue(os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample1.jpg") in files_to_read)
        self.assertTrue(os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample2.pdf") in files_to_read)
