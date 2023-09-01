from flask import Flask, render_template, request, redirect, url_for, flash
from aws_credentials import add_aws_credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    password = request.form['password']

    # Check if the entered credentials are valid
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        # Redirect to home.html if login is successful
        return render_template('home.html', username=username)
    else:
        # Stay on the login page and display failure message
        flash('Invalid credentials', 'failure')
        return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def logout():
    # Perform logout operations here
    # ...
    return render_template('login.html')

# Route to the add_aws_credentials function in aws_credentials.py
@app.route('/aws-credentials/add', methods=['GET', 'POST'])
def add_aws_credentials_route():
    return add_aws_credentials(request)

if __name__ == '__main__':
    app.run(debug=True)
