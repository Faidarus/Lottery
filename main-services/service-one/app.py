from flask import Flask, Response, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
service-two = requests.get('http://localhost:5002/numbers').text
service-three = requests.get('http://localhost:5003/letters').text
service-four = requests.post('http://localhost:5001/winner').text

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')