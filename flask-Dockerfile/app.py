from flask import Flask
app = Flask(__name__)

import os
myvar = os.environ.get('MYVAR')
print(myvar)

a_file = open("/var/secrets/FLASK_SECRET")
file_contents = a_file.read()
print(file_contents)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/fisher')
def hello_fisher():
    return 'Hello, Fisher!'
