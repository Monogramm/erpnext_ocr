# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import unittest

import frappe

from erpnext_ocr.config.desktop import get_data


class TestDesktop(unittest.TestCase):
    def test_get_data(self):
        data = get_data()

        self.assertIsNotNone(data)
