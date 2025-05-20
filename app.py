python
from flask import Flask, request, jsonify
import datetime


app = Flask(__name__)

data = []

@app.route("/signup",methods=['POST'])
def signup():
    # This function will be called when the user clicks the signup button
    if request.method == 'POST':
        x = datetime.datetime.now()
        timestamp = x.strftime("%d%m%Y%H%M%S")
        # Get the data from the form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        dict_json = {"Username":username,"Password":password,"Email":email,"timestamp":timestamp}
        data.append(dict_json)
        return jsonify(message="User Create Successfully", status=200)

@app.route("/formlogin", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        uname = request.form['username']
        password = request.form['user_password']
        if uname == data[0]['Username'] and password == data[0]["Password"]:
            return jsonify(message=f'Wellcome {uname}')
        else:
            return jsonify(message='Invalid Password')
    else:
        return jsonify(message=f'Method is not supported "{request.method}"')

@app.route('/get')
def get():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
