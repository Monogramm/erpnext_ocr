# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# See license.txt

from setuptools import setup, find_packages
import re
import ast

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_autoinstall/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('erpnext_ocr/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='erpnext_ocr',
    version=version,
    description='Optical Character Recognition using tesseract within Frappe..',
    author='Monogramm',
    author_email='opensource@monogramm.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
