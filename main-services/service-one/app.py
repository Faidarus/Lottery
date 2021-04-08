from flask import Flask, Response, request, jsonify

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = getenv
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Lottery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    combined_account_string = db.Column(db.String(50), nullable=False)
    message_string= db.Column(db.String(100), nullable=False)

@app.route('/',methods=['GET', 'POST'])
def home():
    service_two = requests.get('http://localhost:5002/numbers').text
    service_three = requests.get('http://localhost:5003/letters').text
    service_four = requests.post('http://localhost:5001/winner',json={"service_numbers":service_two,"service_letters":service_three}).text
    new_winner = Lottery(combined_account_string = service_four["combined"],  message_string = service_four["message"])
    db.session.add(new_winner)
    db.session.commit()
    return render_template('main.html',title="Lottery",combined_account_string = service_four["combined"], message_string = service_four["message"])


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')