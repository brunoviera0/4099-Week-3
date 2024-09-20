from flask import Flask, request, render_template

app = Flask(__name__)

#route for Address Validation **default**
@app.route('/', methods=['POST', 'GET'])
def address_validation():
    if request.method == 'POST':
        address = request.form['address']
        #assume the address is valid because the js validated it
        success_message = f"Successful! Received Address: {address}"
        return render_template('address.html', success=success_message)
    else:
        return render_template('address.html')

#/password for password validator 
@app.route('/password', methods=['POST', 'GET'])
def password_validation():
    if request.method == 'POST':
        password = request.form['password']
        #assume the password is valid because the js validated it in the html file
        success_message = f"Successful! Password: {password}"
        return render_template('password.html', success=success_message)
    else:
        return render_template('password.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
