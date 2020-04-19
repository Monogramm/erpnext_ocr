# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Fixed

### Removed

<a name="1.1.0"></a>

## 1.1.0 - 2020-04-19

### Added

-   ✨ Add Read OCR to desktop 
-   ✨ Implemented pyspellchecker on OCR results
-   🌐 Add russian translation (#22)
-   ✨ Add default language in OCR Read (#20)
-   ✨ Add read time field (#25)
-   ⚡️ Add background job (#23)
-   ✨ Download new languages (#27)
-   ✨ Text based Doctype import (#26) for #15

### Fixed

-   🔒 Upgrade minimist

<a name="1.0.1"></a>

## 1.0.1 - 2019-11-29

Differences with previous release: [1.0.0...1.0.1](https://github.com/Monogramm/erpnext_ocr/compare/1.0.0...1.0.1)

### Fixed

-   :globe_with_meridians: Fix FR translation for PDF resolution

<a name="1.0.0"></a>

## 1.0.0 - 2019-11-27

Differences with previous release: [0.9.0...1.0.0](https://github.com/Monogramm/erpnext_ocr/compare/0.9.0...1.0.0)

### Added

-   :sparkles: Progress bar during document read
-   :construction_worker: Add unit tests and coverage analysis to CI
-   :sparkles: Read only field to indicate Language available for OCR
-   :sparkles: Add OCR settings

### Changed

-   :wrench: Allow all users to read with OCR
-   :zap: Replace pytesseract by tesserocr

<a name="0.9.0"></a>

## 0.9.0 - 2019-11-06

### Added

-   PDF management in `OCR Read`
-   `OCR Language` to manage available tesseract traindata files
-   French translations
-   GitHub issue and feature templates
-   GitHub bots config ([stale](https://github.com/apps/stale) and [behaviorbot](https://github.com/behaviorbot))
-   [Travis-CI](https://travis-ci.org/) using [docker images](https://github.com/Monogramm/docker-erpnext) to setup ERPNext test environment
-   Contributing guidelines
-   This CHANGELOG file to hopefully help to track changes done to the project.

### Changed

-   PIP requirements for easier (auto) install
-   README documentation on requirements, installation and common issues
-   Desktop icon, color, name and docs
-   Repository name (changed case)
-   Author/maintainer info

### Fixed

-   Python 3 compatibility
-   Management of public/private files upload

### Removed

-   Sales Invoice custom fields and scripts
-   OCR Receipt for Sales Invoice
-   ABBYY OCR
-   Zapier webhook
-   Aimara / jstree / treeview

## Legacy - 2018-02-12

### Added

-   All the good work from [John Vincent Fiel](https://github.com/jvfiel) on the source of this project.

Source of fork: [jvfiel/ERPNext-OCR](https://github.com/jvfiel/ERPNext-OCR/tree/master)
