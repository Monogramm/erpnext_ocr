# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# For license information, please see license.txt

import unittest

from erpnext_ocr.config.docs import get_context


class TestDocs(unittest.TestCase):
    def test_get_context(self):
        context = type('obj', (object,), {'brand_html' : None,
                                          'source_link' : None,
                                          'docs_base_url' : None,
                                          'headline' : None,
                                          'sub_heading' : None})
        get_context(context)

        self.assertIsNotNone(context)
        self.assertIsNotNone(context.brand_html)
        self.assertIsNotNone(context.source_link)
        self.assertIsNotNone(context.docs_base_url)
        self.assertIsNotNone(context.headline)
        self.assertIsNotNone(context.sub_heading)
