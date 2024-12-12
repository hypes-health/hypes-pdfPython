def getAge(pdf_path):
    import pdfplumber
    import re
    with pdfplumber.open(pdf_path) as pdf:
        pages_to_search=range(0,1)
        for page_number in pages_to_search:
            page = pdf.pages[page_number]
            text = page.extract_text()
            params='Age'
            param_pattern = re.compile(rf'(?:^|[\s:()\-=\/]){params}(?:$|[\s:()\-=\/])', re.IGNORECASE)
            match = param_pattern.search(text)
            if match:
                param_text = text[match.end():]
                value_match = re.search(r'\d+(\.\d+)?', param_text)
                if value_match:
                    value = re.sub(r'[^\d.]', '', value_match.group())
                    return float(value)
    return "N/A"

