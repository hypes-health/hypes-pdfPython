from openai import OpenAI
from Entity.params import prms
from flask import jsonify
import pdfplumber
import json
import ast
import pandas as pd
client = OpenAI(
    api_key="<API-KEY>"
)
def gooo(pdf_path):
  ans='{}'
  ans=json.loads(ans)
  with pdfplumber.open(pdf_path) as pdf:
    text=""
    for pgno in range(0,len(pdf.pages)):
      page=pdf.pages[pgno]
      text=text+page.extract_text()
    # print(prms)
    try:
      # print(text)
      completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
          {"role": "user",
           "content": f'{text} save this as blood report and Extract all parameters with numerical values (including percentages, absolute counts, ratios, and measurements) from the provided blood report alonbg with name,gender,age, reportedon,Use subheadings, headings, and context to identify parameter names, and return as JSON in the format:json '
                      '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'}]

      # "content": f'{text} save this as blood report and after trying to orient in proper way search for all parameters which have values (there could be 2 values in single row check for everything using orientation, headings and subheadings), use sub headings to define parameter name clearly, show me which are found as single python list of names and no other text'}]
                      # f'then search for every parameters one by one in sequence from parameters list in report if found parameter with same meaning, full form, short form and not null value found then give all that names from parameters list in json result ignoring all other text or char just the json'}]
                      # f'add parameter in final result json with exact name as mentioned in parameters list, strictly dont add parameters which are not mentioned in parameters list carefully, ignoring all other text or char just the json'}]
      )
    except Exception as e:
      print(e)
    demoo=completion.choices[0].message.content
    print("demoo :",demoo)
    clean_content = demoo.strip("```json").strip("```").strip()

    # clean_content = demoo.strip("```json").strip("```").strip()
    try:
      tempans=pd.read_json(clean_content, typ = 'series').to_dict()
      completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
          {"role": "user",
           "content": f'{tempans} save this as blood report analysis and {prms} as parameters list, and find parameters with similar names from parameters list and create a resulting json which should always have same names from parameter list and have not null value in analysis in the format:json '
                      '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'}]

      # "content": f'{text} save this as blood report and after trying to orient in proper way search for all parameters which have values (there could be 2 values in single row check for everything using orientation, headings and subheadings), use sub headings to define parameter name clearly, show me which are found as single python list of names and no other text'}]
                      # f'then search for every parameters one by one in sequence from parameters list in report if found parameter with same meaning, full form, short form and not null value found then give all that names from parameters list in json result ignoring all other text or char just the json'}]
                      # f'add parameter in final result json with exact name as mentioned in parameters list, strictly dont add parameters which are not mentioned in parameters list carefully, ignoring all other text or char just the json'}]
      )
      # tempans=json.loads(clean_content)
      demoo = completion
      print("demoo :", demoo)
      # clean_content = demoo.strip("```json").strip("```").strip()
      # tempans = pd.read_json(clean_content, typ='series').to_dict()
      ans=tempans
      # print("tepansfe :",tempans)
      # ans={**ans,**tempans}
    except Exception as e:
      print("exception: ",e)
    # print(type(clean_content))

  return ans
