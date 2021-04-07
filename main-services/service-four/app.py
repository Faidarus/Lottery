from flask import Flask, Response, request, jsonify
import random
import string

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Manchester123!@35.189.66.154/..."
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Lottery_form(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Add Name')


@app.route('/lottery',methods=['GET'])
def winner():
combined_lists = ""
prize = 250
number_choice = [1, 3, 5, 7, 9]
service-two = requests.get('http://localhost:5002/numbers').text
service-three = requests.get('http://localhost:5003/letters').text
combined_lists = numbers + letters
random.choice(number_choice) 
for f in range (len(combined_lists)):
    if random.choice(number_choice) = 5 in combined_lists:
        won = prize
        



db.create_all()
db.session.add(winner)
db.session.commit()

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')