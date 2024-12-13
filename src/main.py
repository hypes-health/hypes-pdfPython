from logging import error

from Controller.routes import pdf
from flask import Flask, request

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)