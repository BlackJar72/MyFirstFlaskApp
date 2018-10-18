from flask import Flask, render_template, redirect, url_for
import sys, os

app = Flask(__name__)

fragnames = os.listdir("templates/frament")
fragdict = {}
for fname in fragnames: 
  with open(fname, r) as f:
    fragdict[fname] = f.read()

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

@app.route('/poetry/', methods=['GET', 'POST'])
def poempage():
    if request.method = 'GET':
      title = request.args.get('poem')
      if title != None:
	return render_template('poetry.html', poem=fragdict[title])
      else
	return render_template('poetry.html', poem='')    
    return render_template('poetry.html', poem='')

@app.route('/art/')
def artpage():
    return underConstruction()

@app.route('/music/')
def musicpage():
    return render_template("music.html")

@app.route('/bio/')
def biopage():
    return underConstruction()

@app.route('/resume/')
def resumepage():
    return render_template("resume.html")

@app.route('/contact/')
def contactpage():
    return underConstruction()
  
@app.errorhandler(404)
def handle404(e):
  return render_template("404.html")


#Start the who thing running!!!
if __name__ == "__main__":
    app.run(host='0.0.0.0')

