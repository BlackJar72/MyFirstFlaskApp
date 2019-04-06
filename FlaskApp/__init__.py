from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
import sys, os

'''
FIXME: This is growing large and unwieldy.
I need to look into modularizing this.
'''

app = Flask(__name__)
mail_settings = {}

fragnames = os.listdir("templates/frament")
fragdict = {}
for fname in fragnames:
  with open("templates/frament/" + fname, 'r') as f:
    fragdict[fname] = f.read()


def readDatFile(name):
  f = open("../../../dat/" + name)
  out = f.read()
  f.close()
  return out


def setupMail():
  pw = readDatFile('fmgmpw')
  nm = readDatFile('fmgmui')
  sv = readDatFile('fmgmsv')
  mail_settings = {
    "DEBUG" : False,
    "MAIL_SERVER" : sv,
    "MAIL_PORT" : 587,
    "MAIL_USE_TLS" : True,
    "MAIL_USERNAME" : nm,
    "MAIL_PASSWORD" : pw
  }
  app.config.update(mail_settings)
  print(mail_settings)
  return Mail(app)

mail = setupMail()
mailRecipient = readDatFile('fmgmrp')
mailSender    = readDatFile('fmgmsd')


@app.route('/sendmail/', methods=['GET', 'POST'])
def sendMail():
  if request.method == 'POST':
    title = request.form['title']
    sender = request.form['name']
    email = request.form['email']
    body = request.form['body']
    try:
      msg = Message("[KF:MSG] {0}".format(title),
	    sender=mailSender,
	    recipients=[mailRecipient])
      msg.body = "From: {0}  ({1}) \n\n{2}".format(sender, email, body)
      mail.send(msg)
      return render_template("mail-sent.html")
    except Exception as e:
      f = open("../../../log/errors.log", 'a')
      f.write(str(e) + '\n')
      f.write(request.form)
      f.write('\n')
      f.write(mail_settings)
      f.write('\n\n')
      return render_template("mail-fail.html")
  else:
    return render_template("mail-fail.html")


def underConstruction():
  return render_template("unfinished.html")


@app.route('/')
def homepage():
    return render_template("mail.html")


@app.route('/projects/')
def projpage():
    return render_template("mail.html")


@app.route('/games/')
def gamespage():
    return redirect(url_for('projpage',_anchor='games'))


@app.route('/desktop/')
def desktoppage():
    return redirect(url_for('projpage',_anchor='desktop'))


@app.route('/poetry/', methods=['GET', 'POST'])
def poempage():
    if request.method == 'GET':
      title = request.args.get('poem')
      if title != None and title in fragdict:
        return render_template('poetry.html', poem=fragdict[title])
      else:
        return render_template('poetry.html', poem='')
    return render_template('poetry.html', poem='')


@app.route('/art/')
def artpage():
    return underConstruction()


@app.route('/music/')
def musicpage():
    return render_template("mail.html")


@app.route('/bio/')
def biopage():
    return render_template("mail.html")


@app.route('/resume/')
def resumepage():
    return render_template("mail.html")


@app.route('/contact/')
def contactpage():
    return render_template("mail.html")

  
@app.errorhandler(404)
def handle404(e):
  return render_template("404.html")


#Start the whole thing running!!!
if __name__ == "__main__":
  app.run(host='0.0.0.0')

