from flask import Flask, render_template
import sys

app = Flask(__name__)

def underConstruction():
  return render_template("unfinished.html")

@app.route('/flask/')
def homepage():
    #return underConstruction()
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

