from flask import Flask, Response, request, jsonify
 from random import randit
app = Flask(__name__)

@app.route('/numbers',methods=['GET'])

empty_list = []
def numbers():
    empty_list_two = []

    for f in range(6): # asking for a range loop of six numbers
        a = random.randint(1,10) #returns a number between 1 and 10
        empty_list.append(a) # adding random numbers to empty list
    return empty_list
print(numbers())

        # return response = requests.get('https://34.105.144.222:5002', data='my data')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')