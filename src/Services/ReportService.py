from openai import OpenAI
from Entity.params import prms
from flask import jsonify
import pdfplumber
import json
import ast
import pandas as pd
client = OpenAI(
    api_key="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"
)
def ExtractReport(pdf_path):
  ans='{}'
  ans=json.loads(ans)
  with pdfplumber.open(pdf_path) as pdf:
    text=""
    for pgno in range(0,len(pdf.pages)):
      page=pdf.pages[pgno]
      text=text+page.extract_text()
    try:
      completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
          {"role": "user",
           "content": f'{text} save this as blood report and Extract all parameters with numerical values (including percentages, absolute counts, ratios, and measurements) from the provided blood report alonbg with name,gender,age, reportedon,Use subheadings, headings, and context to identify parameter names, and return as JSON in the format:json '
                      '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'}]
      )
      response=completion.choices[0].message.content
      clean_content = response.strip("```json").strip("```").strip()
      response=pd.read_json(clean_content, typ = 'series').to_dict()
      print(len(response))
      completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
          {"role": "user",
           "content": f'{response} save this as blood report analysis and {prms} as parameters list, and find parameters with similar names from parameters list and create a resulting json which should always have same names from parameter list and have not null value in analysis (also focus on name,age,gender, reportedOn parameter) in the format:json '
                      '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'}]
      )
      response= completion.choices[0].message.content
      clean_content = response.strip("```json").strip("```").strip()
      response = pd.read_json(clean_content, typ='series').to_dict()
      ans=response
    except Exception as e:
      print("exception: ",e)

  return ans