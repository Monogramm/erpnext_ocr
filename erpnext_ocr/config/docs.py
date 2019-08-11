"""
Configuration for docs
"""

# source_link = "https://github.com/[org_name]/erpnext_ocr"
# docs_base_url = "https://[org_name].github.io/erpnext_ocr"
# headline = "App that does everything"
# sub_heading = "Yes, you got that right the first time, everything"

def get_context(context):
	context.brand_html = "ERPNext OCR"
	context.source_link = "https://github.com/Monogramm/erpnext_ocr"
	context.docs_base_url = "https://github.com/Monogramm/erpnext_ocr"
	context.headline = "OCR Integration"
	context.sub_heading = "Optical Character Recognition using tesseract within ERPNext"
