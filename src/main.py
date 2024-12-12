from Controller.routes import pdf
from flask import Flask,request

app = Flask(__name__)

@app.route('/health-check',methods=['GET'])
def hello_world():
    return "Health Okay"

@app.route('/pdf',methods=['GET'])
def pdfProcess():
    pdf_path=request.args.get('pdf_path')
    return pdf(pdf_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)