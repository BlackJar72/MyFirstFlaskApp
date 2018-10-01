from flask import Flask, render_template, redirect, url_for
import sys

app = Flask(__name__)

def underConstruction():
  return render_template("unfinished.html")

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/projects/')
def projpage():
    return render_template("projects.html")

@app.route('/games/')
def gamespage():
    return redirect(url_for('projpage',_anchor='games'))

@app.route('/desktop/')
def desktoppage():
    return redirect(url_for('projpage',_anchor='desktop'))

@app.route('/poetry/')
def poempage():
    return underConstruction()

@app.route('/art/')
def artpage():
    return underConstruction()

@app.route('/music/')
def musicpage():
    return underConstruction()

@app.route('/bio/')
def biopage():
    return underConstruction()

@app.route('/resume/')
def resumepage():
    return render_template("resume.html")

@app.route('/contact/')
def contactpage():
    return underConstruction()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

