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
          {
            "role": "system",
            "content": "You are a data extractor whose primary job is to extract parameters and their numerical values from blood reports. Ensure you use proper naming conventions for parameters and provide the output in a clean, structured JSON format."
          },
          {
            "role": "system",
            "content": f"Save this as the blood report text. {text}"
          },
          {
            "role": "system",
            "content": "analyze the blood report context thoroughly. Go through each and every parameter in the report, one by one, and extract parameters that have numerical values including percentages, absolute counts, ratios (convert raitos into decimal), and measurements. Additionally, extract information such as name, gender, age, and reported date"
          },
          {
            "role": "user",
            "content": "convert ratios into decimal and store it as decimal value"
          },
          {
            "role":"user",
            "content":f'Strictly use subheadings, headings, and context to identify parameter names accurately. Ensure parameter names are descriptive and use long, informative naming conventions based on the available information in the report'
          },
          {
            "role": "user",
            "content": 'return as JSON in the format:json '
                      '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'
          }
        ]
          # {"role": "user",
          #  "content": f'{text} save this as blood report and Extract all parameters with numerical values (including percentages, absolute counts, ratios, and measurements) from the provided blood report alonbg with name,gender,age, reportedon,Use subheadings, headings, and context to identify parameter names, and return as JSON in the format:json '
          #             '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'}]
      )
      response=completion.choices[0].message.content
      clean_content = response.strip("```json").strip("```").strip()
      response=pd.read_json(clean_content, typ = 'series').to_dict()
      print(len(response))
      print(response)
      completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[

          {
            "role": "system",
            "content": "You are a name-matching assistant. Your role is to accurately match parameters from a given parameters names list with a response from a blood report analysis. The final response should only contain names from the parameters names list."
          },
          {
            "role": "system",
            "content": "Match parameter names using short forms, full forms, synonyms, and similar names. Use intelligent pattern matching to ensure names that are conceptually similar are matched accurately. Ignore differences in letter case (e.g., uppercase or lowercase).Verify thoroughly to ensure that each parameter in the blood report analysis is mapped to the most comparable name from the parameters names list. Ensure all fields, including general ones like name, age, sex, and reportedOn, are included in the final output"
          },
          {
            "role": "system",
            "content": f"Save the following as blood report analysis: {response} and Save the following as parameters names list: {prms}"
          },
          {
            "role": "user",
            "content": "Check every parameter from the blood report analysis against the parameters names list. Ensure names with minor variations, such as underscores vs. spaces, abbreviations, or plural/singular forms, are matched accurately."
          },
          {
            "role": "user",
            "content": 'return as JSON in the format:json '
                       '{"parameter": value,"parameter2": value2} and no other sub objects, with no other text'
          }
          ]
      )
      response= completion.choices[0].message.content
      clean_content = response.strip("```json").strip("```").strip()
      response = pd.read_json(clean_content, typ='series').to_dict()
      print(response)
      ans=response
    except Exception as e:
      print("exception: ",e)

  return ans