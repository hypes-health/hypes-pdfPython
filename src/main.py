from logging import error

from Controller.routes import pdf
from flask import Flask, request
from OCR.OCR import gooo
from Entity.final_demo import decode_polyline_text,finalll
from Entity.checkkk import lpi
from Entity.limits import limits
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
def pdfPP():
    try:
        if len(request.files.keys()):
            key="pdf"
            for name in request.files:
                key=name
                break
            file = request.files[key].stream
            return gooo(file)
            return "rfdc"
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)