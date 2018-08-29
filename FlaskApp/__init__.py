from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/flask/')
def homepage():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

