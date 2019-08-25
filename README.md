
[uri_license]: https://opensource.org/licenses/MIT
[uri_license_image]: https://img.shields.io/badge/license-MIT-blue

[![License: MIT][uri_license_image]][uri_license]
[![Managed with Taiga.io](https://img.shields.io/badge/managed%20with-TAIGA.io-709f14.svg)](https://tree.taiga.io/project/monogrammbot-monogrammerpnext_ocr/ "Managed with Taiga.io")
[![Docker Automated buid](https://img.shields.io/docker/cloud/build/monogrammbot/erpnext_ocr.svg)](https://hub.docker.com/r/monogrammbot/erpnext_ocr/)


## ERPNext OCR

OCR with [tesseract](https://github.com/tesseract-ocr/tesseract).

#### License

MIT# ERPNext-OCR

## About this project

This project is a fork of [ERPNext-OCR](https://github.com/jvfiel/ERPNext-OCR) by John Vincent Fiel.
Its aim is to fix and cleanup the original source code.

**Changes**
* See [CHANGELOG](./CHANGELOG.md)


**Roadmap**
* Implement [Frappe unit tests](https://frappe.io/docs/user/en/guides/automated-testing/unit-testing) using content of tesseract directory
* Add [Travis-CI](https://travis-ci.org/) using [docker images](https://github.com/Monogramm/docker-erpnext) to setup ERPNext test environment
* Add the possibility to download new [Tesseract languages](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files)
* Use a background job and display popup while reading the document
* Add a spell checker to improve the read results


## Sample Screenshot
![Sample Screenshot](https://github.com/jvfiel/ERPNext-OCR/blob/master/erpnext_ocr/erpnext_ocr/Selection_046.png)

## File Being Read
![Sample Screenshot 2](https://github.com/jvfiel/ERPNext-OCR/blob/master/erpnext_ocr/erpnext_ocr/Selection_047.png)


## Pre-requisites: tesseract-python and imagemagick

- Install tesseract-ocr, plus imagemagick and ghostscript (to work with pdf files) using this command on Debian:
  ```
  sudo apt-get install tesseract-ocr imagemagick libmagickwand-dev ghostscript
  ```

## Installation

  ```
  bench get-app --branch develop erpnext_ocr https://github.com/Monogramm/erpnext_ocr
  bench install-app erpnext_ocr
  ```

When installing Frappe app, the following python requirements will be installed:
* python binding for tesseract, [pytesseract](https://pypi.org/project/pytesseract/)
* image processing library in python, [pillow](https://pypi.org/project/Pillow/)
* HTTP library in python, [requests](https://pypi.org/project/requests/)
* python binding for imagemagick, [wand](https://pypi.org/project/Wand/)

## Tesseract trained data

In order to use OCR with different languages, you need to install the appropriate trained data files.
Check tesseract Wiki for details https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

## Known issues

* `wand.exceptions.PolicyError: not authorized '/opt/sample.pdf' @ error/constitute.c/ReadImage/412`
    * This can happen due to security configuration in imagemagick, preventing it to read PDF files.
    * Reference:
        * https://stackoverflow.com/questions/52699608/wand-policy-error-error-constitute-c-readimage-412
        * https://stackoverflow.com/questions/42928765/convertnot-authorized-aaaa-error-constitute-c-readimage-453
* `wand.exceptions.WandRuntimeError: MagickReadImage returns false, but did raise ImageMagick exception. This can occurs when a delegate is missing, or returns EXIT_SUCCESS without generating a raster.`
    * This might happen if you're missing a dependency to convert PDF, most of the time `ghostscript`
    * References:
        * https://stackoverflow.com/questions/57271287/user-wand-by-python-to-convert-pdf-to-jepg-raise-wand-exceptions-wandruntimeerr
* `OSError: encoder error -2 when writing image file`
    * This might happen when trying to open a TIFF image, but the real error is "_hidden_" and only displayed in console.
    * If the original error in console is `Fax3SetupState: Bits/sample must be 1 for Group 3/4 encoding/decoding.` that usually happens when TIFF image compression is not valid / recognized.
