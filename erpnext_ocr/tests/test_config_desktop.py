# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# For license information, please see license.txt

import unittest

from erpnext_ocr.config.desktop import get_data


class TestDesktop(unittest.TestCase):
    def test_get_data(self):
        data = get_data()

        self.assertIsNotNone(data)
