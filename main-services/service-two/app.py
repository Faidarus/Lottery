from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/numbers',methods=['GET'])
def numbers():
    empty_list = "" #modified my list into string because it will not run on lists 
    for f in range(6): # asking for a range loop of six numbers
        a = random.randint(1,10) #returns a number between 1 and 10
        empty_list += str(a) # adding random numbers to empty string list
    return empty_list
print(numbers())


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')