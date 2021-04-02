from flask import Flask, Response, request, jsonify
from random import randinit
import string

app = Flask(__name__)

@app.route('/lottery',methods=['GET'])
def lottery():

service-two = requests.get('http://localhost:5002')
service-three = requests.get('http://localhost:5003')


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')