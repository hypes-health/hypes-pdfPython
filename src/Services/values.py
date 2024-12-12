import pdfplumber
import re

from ..Entity.result import results

def locate_test_page(pdf, test_name):
    test_pattern = re.compile(rf'(?:^|[\s:()\-=\/]){test_name}(?:$|[\s:()\-=\/])', re.IGNORECASE)
    for page_number, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if test_pattern.search(text):
            return page_number
    return -1
def getValues(pdf_path, test_name, parameters, page_range):
    with pdfplumber.open(pdf_path) as pdf:

        test_page=-1
        for name in test_name:
          test_page = locate_test_page(pdf,name)
          if test_page==-1:
            continue
          else:
            break
        if test_page==-1:
            return
        max_pages = len(pdf.pages)
        pages_to_search = range(test_page-1,min(test_page- 1+page_range,max_pages))
        for page_number in pages_to_search:
            page = pdf.pages[page_number]
            text = page.extract_text()
            for params in parameters:
              if results["parameters"][params]["value"] is not None:
                    continue
              for param in parameters[params]:
                if results["parameters"][params]["value"] is not None:
                    break
                param_pattern = re.compile(rf'(?:^|[\s:()\-=]){param}(?:$|[\s:()\-=])', re.IGNORECASE)

                match = param_pattern.search(text)
                if match:
                    param_text = text[match.end():]
                    value_match = re.search(r'\d+(\.\d+)?', param_text)
                    if value_match:
                        value = re.sub(r'[^\d.]', '', value_match.group())
                        results["parameters"][params]["value"] = float(value)
                        break
