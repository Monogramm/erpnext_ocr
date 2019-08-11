## ERPNext OCR

OCR with [tesseract](https://github.com/tesseract-ocr/tesseract).

#### License

MIT# ERPNext-OCR

## Sample Screenshot
![Sample Screenshot](https://github.com/jvfiel/ERPNext-OCR/blob/master/erpnext_ocr/erpnext_ocr/Selection_046.png)

## File Being Read
![Sample Screenshot 2](https://github.com/jvfiel/ERPNext-OCR/blob/master/erpnext_ocr/erpnext_ocr/Selection_047.png)


## Pre-requisites: tesseract-python and imagemagick

- Install tesserct-ocr and imagemagick (to work with pdf files) using this command on Debian:
  ```
  sudo apt-get install tesseract-ocr imagemagick libmagickwand-dev
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
