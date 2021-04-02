from flask import Flask, Response, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():

service-four = requests.get('http://localhost:5001')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')