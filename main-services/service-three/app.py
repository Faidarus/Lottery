from flask import Flask, Response, request, jsonify
from random import randinit
import string 
app = Flask(__name__)

empty_letter_list=[]
def letters():
   letter_amount = 8 #how many leters I want to generate 
   uppercase_letters = "".join(random.choice(string.ascii_uppercase) for i in range(letter_amount)) #genrates random uppercase letters with the range of 8 highlighted in letter amount
   empty_letter_list.append(uppercase_letters) # will join the the range with letter amount 
   return empty_letter_list # returns the empty_list
print(letters())


if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')