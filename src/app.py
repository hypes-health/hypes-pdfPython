from logging import error
from docx import Document
from Controller.routes import pdf
from flask import Flask, request
from Services.ReportService import ExtractReport
from Entity.checkkk import lpi
from Entity.limits import limits
from Controller.GptInterface import Gpt
from Entity.final_demo import opq
import json
# from OCR.OCR import
app = Flask(__name__)

@app.route('/health-check',methods=['GET'])
def hello_world():
    return "Health Okay"
@app.route('/pdf',methods=['POST'])
def pdfProcess():
    try:
        if len(request.files.keys()):
            key="pdf"
            for name in request.files:
                key=name
                break
            file = request.files[key].stream
            return pdf(file)
    except Exception as e:
        error(e)

@app.route('/pdf-check',methods=['POST'])
def pdfCheck():
    for sno in range(1,112):
        pdfPP(f"G:\\reports zip\\Blood Reports\\report_{sno}.pdf",sno)
    return "done"

def pdfPP(pdfpath,sno):
    try:
        # response=str(pdf(pdfpath))#.toString()
        content=pdf(pdfpath)
        content = json.dumps(content, indent=4)
        file_name=f"G:\\reports zip\\Reports Output\\report{sno}.docx"
        file_name=str(file_name)
        """
        Creates a new file with the given name and writes the content to it.

        Args:
            file_name (str): The name of the file to create.
            content (str): The content to write into the file.
        """
        try:
            # Create a new Word document
            doc = Document()

            # Add content to the document
            doc.add_paragraph(content)

            # Save the document
            doc.save(file_name)
            print(f"File '{sno}' created successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")




    except Exception as e:
        error(e)
@app.route('/param-check',methods=['POST'])
def pdP():
    try:
        for key in lpi:
            if(len(limits[key])>0):
                print(key, limits[key]['M']["lower"])
            else:
                print(key)
        return "okay"
    except Exception as e:
        error(e)
@app.route('/gpt/<message>',methods=['POST'])
def gpt(message):
    try:
        return Gpt(message)
        return message
        # return "okay"
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)