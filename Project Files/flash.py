
from flask import Flask, render_template

app = Flask(_name_)

@app.route('/templates')
def dashboard():
    return render_template('index.html')