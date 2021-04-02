from flask import Flask, Response, request, jsonify
from random import randinit
import string 
app = Flask(__name__)

@app.route('/numbers',methods=['GET'])
def numbers():
   letter_amount = 8
   uppercase_letters = "".join(random.choice(string.ascii_uppercase) for i in range(letter_amount))
#    lowercase_letters = "".join(random.choice(string.ascii_lowercase) for i in range(letter_amount))


return uppercase_letters
# return lowercase_letters


if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')