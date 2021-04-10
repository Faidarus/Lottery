from flask import Flask, Response, request, jsonify
import random
import string

app = Flask(__name__)
@app.route('/lottery',methods=['POST'])
def winner():
    prize = 500 #predefined variable
    won = 0
    message = f"You didn't win £{won}"
    number_choice = ["2","4","6","8","10"]
    data = request.get_json()
    combined_lists = data["service_numbers"] + data["service_letters"] #combined services into one variable
    if random.choice(number_choice) == combined_lists[2] or random.choice(number_choice) == combined_lists[4]: #Check to see if there is a random number in specific index value
        won += prize/2  #adds half the prize to the current winnings
        message = f"Congratulation you won £{won}" #change the message
    return jsonify({"combined":combined_lists,"message":message})


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')