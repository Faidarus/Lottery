from flask import Flask, Response, request, jsonify
import random
import string

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@35.189.66.154/..."
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Lottery_form(FlaskForm):
    third_name = StringField('Name')
    submit = SubmitField('Add Name')


@app.route('/lottery',methods=['GET'])
def winner():

service-two = requests.get('http://localhost:5002/numbers').text
service-three = requests.get('http://localhost:5003/letters').text


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')