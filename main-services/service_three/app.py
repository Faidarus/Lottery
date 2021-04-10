from flask import Flask,request
import random
import string 


app = Flask(__name__)

@app.route('/letters',methods=['GET'])
def letters():
   empty_letter_list="" #modified my list into string because it will not run on lists 
   letter_amount = 4 #the amount of letters you want 
   lowercase_letters = "".join(random.choice(string.ascii_uppercase) for i in range(letter_amount)) #will generate 8 random letters
   empty_letter_list += lowercase_letters #adding uppercase letters to emptylist
   return empty_letter_list
print(letters())


if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')