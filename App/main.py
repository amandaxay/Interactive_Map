from flask import Flask
from flask import render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('/landing.html') 


@app.route('/CAstatePage')
def CAstate():
    return render_template('/CAstatePage.html')

@app.route('/ORstatePage')
def ORstate():
    return render_template('/ORstatePage.html')

@app.route('/WAstatePage')
def WAstate():
    return render_template('/WAstatePage.html')

@app.route('/PAstatePage')
def PAstate():
    return render_template('/PAstatePage.html')

@app.route('/NYstatePage')
def NYstate():
    return render_template('/NYstatePage.html')

@app.route('/FLstatePage')
def FLstate():
    return render_template('/FLstatePage.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/journal')
def journal():
    return render_template('/journal.html')

@app.route('/map')
def signin():
    return render_template('/index.html')


if __name__ == "__main__":
    app.run(debug=True)