from flask import Flask, Response, request, jsonify
 from random import randinit
app = Flask(__name__)

@app.route('/numbers',methods=['GET'])
def numbers():
    empty_list = []
    # empty_list_two = []

    for f in range(6): # asking for a range loop of six numbers
        a = random.randit(1,10) #returns a number between 1 and 10
        empty_list.append(a) # adding random numbers to empty list

return empty_list
    
    # for l in range(8):
    # z = random.randint(10,20)
    # empty_list_two.append(z)


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')