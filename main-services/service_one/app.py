from flask import Flask, Response, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy 
import requests
import random
import string
from os import getenv
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Lottery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    combined_account_string = db.Column(db.String(50), nullable=False)
    message_string= db.Column(db.String(100), nullable=False)

@app.route('/',methods=['GET', 'POST'])
def home():
    service_two = requests.get('http://service_two:5002/numbers').text
    service_three = requests.get('http://service_three:5003/letters').text
    service_four = requests.post('http://service_four:5001/lottery', json={"service_numbers":service_two,"service_letters":service_three}).json()
    new_winner = Lottery(combined_account_string = service_four["combined"],  message_string = service_four["message"])
    db.session.add(new_winner)
    db.session.commit()
    return render_template('main.html',title="Lottery",combined_account_string = service_four["combined"], message_string = service_four["message"])


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')