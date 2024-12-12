def getGender(pdf_path):
    import pdfplumber
    import re
    keywords = ["Gender", "Sex"]
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            for keyword in keywords:
                keyword_pattern = re.compile(rf'[^\w]*{keyword}[^\w]*', re.IGNORECASE)
                match = keyword_pattern.search(text)
                if match:
                    param_text = text[match.end():]
                    for char in param_text:
                        char = char.upper()
                        if char == "M":
                            return "M"
                        elif char == "F":
                            return "F"

    return "M"