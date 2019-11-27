[uri_license]: https://opensource.org/licenses/MIT

[uri_license_image]: https://img.shields.io/badge/license-MIT-blue

[![License: MIT][uri_license_image]][uri_license]
[![Managed with Taiga.io](https://img.shields.io/badge/managed%20with-TAIGA.io-709f14.svg)](https://tree.taiga.io/project/monogrammbot-monogrammerpnext_ocr/ "Managed with Taiga.io")
[![Build Status](https://travis-ci.org/Monogramm/erpnext_ocr.svg)](https://travis-ci.org/Monogramm/erpnext_ocr)
[![Coverage Status](https://coveralls.io/repos/github/Monogramm/erpnext_ocr/badge.svg?branch=master)](https://coveralls.io/github/Monogramm/erpnext_ocr?branch=master)

## ERPNext OCR

> :alembic: **Experimental** Frappe OCR application with [tesseract](https://github.com/tesseract-ocr/tesseract).

This project is a fork of [ERPNext-OCR](https://github.com/jvfiel/ERPNext-OCR) by [John Vincent Fiel](https://github.com/jvfiel). Its aim is to fix and cleanup the original source code and add some new features.

Check out more on [ERPNext Discuss](https://discuss.erpnext.com/t/erpnext-ocr-app/33834/7).

## :chart_with_upwards_trend: Changes

See [CHANGELOG](./CHANGELOG.md)

## :bookmark: Roadmap

See [Taiga.io](https://tree.taiga.io/project/monogrammbot-monogrammerpnext_ocr/ "Taiga.io monogrammbot-monogrammerpnext_ocr")

## :construction: Install

**Pre-requisites: tesseract-python and imagemagick**

Install tesseract-ocr, plus imagemagick and ghostscript (to work with pdf files) using this command on Debian:

```sh
sudo apt-get install tesseract-ocr imagemagick libmagickwand-dev ghostscript
```

**Install Frappe application**

```sh
bench get-app --branch develop erpnext_ocr https://github.com/Monogramm/erpnext_ocr
bench install-app erpnext_ocr
```

When installing Frappe app, the following python requirements will be installed:

-   python binding for tesseract, [tesserocr](https://pypi.org/project/tesserocr/)

-   image processing library in python, [pillow](https://pypi.org/project/Pillow/)

-   HTTP library in python, [requests](https://pypi.org/project/requests/)

-   python binding for imagemagick, [wand](https://pypi.org/project/Wand/)

## :rocket: Usage

**File Being Read**:

![File Being Read](./erpnext_ocr/tests/test_data/Picture_010.png)

**Sample Screenshot**:

![Sample Screenshot](./erpnext_ocr/tests/test_data/Picture_010_screenshot.png)

### Tesseract trained data

In order to use OCR with different languages, you need to install the appropriate trained data files.
Check tesseract Wiki for details: <https://github.com/tesseract-ocr/tesseract/wiki/Data-Files>

### Known issues

-   `wand.exceptions.PolicyError: not authorized '/opt/sample.pdf' @ error/constitute.c/ReadImage/412`
    -   This can happen due to security configuration in imagemagick, preventing it to read PDF files.
    -   Reference:
        -   <https://stackoverflow.com/questions/52699608/wand-policy-error-error-constitute-c-readimage-412>
        -   <https://stackoverflow.com/questions/42928765/convertnot-authorized-aaaa-error-constitute-c-readimage-453>
-   `wand.exceptions.WandRuntimeError: MagickReadImage returns false, but did raise ImageMagick exception. This can occurs when a delegate is missing, or returns EXIT_SUCCESS without generating a raster.`
    -   This might happen if you're missing a dependency to convert PDF, most of the time `ghostscript`
    -   References:
        -   <https://stackoverflow.com/questions/57271287/user-wand-by-python-to-convert-pdf-to-jepg-raise-wand-exceptions-wandruntimeerr>
-   `OSError: encoder error -2 when writing image file`
    -   This might happen when trying to open a TIFF image, but the real error is "_hidden_" and only displayed in console.
    -   If the original error in console is `Fax3SetupState: Bits/sample must be 1 for Group 3/4 encoding/decoding.` that usually happens when TIFF image compression is not valid / recognized.

## :white_check_mark: Run tests

```sh
bench bench run-tests --profile --app erpnext_ocr
```

## :bust_in_silhouette: Authors

**Monogramm**

-   Website: <https://www.monogramm.io>
-   Github: [@Monogramm](https://github.com/Monogramm)

**John Vincent Fiel**

-   Github: [@jvfiel](https://github.com/jvfiel)

## :handshake: Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Monogramm/erpnext_ocr/issues).
[Check the contributing guide](./CONTRIBUTING.md).<br />

## :thumbsup: Show your support

Give a :star: if this project helped you!

## :page_facing_up: License

Copyright © 2019 [Monogramm](https://github.com/Monogramm).<br />
This project is [MIT](uri_license) licensed.

* * *

_This README was generated with :heart: by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
