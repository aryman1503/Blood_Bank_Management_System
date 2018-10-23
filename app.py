from flask import Flask, render_template, redirect, flash, url_for, session, request, logging
from data import Articles
import sqlite3 as MySQL
from flaskext.mysql import MySQL
#from flask_mysql import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

#if __name__ == '__main__':
#    main()
app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donarreg')
def donarreg():
    return render_template('donarreg.html')

@app.route('/ngo')
def ngo():
    return render_template('ngo.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/registration')
def register():
    return render_template('register.html')
#class RegistrationForm(Form):
  #  name = StringField('Name', [validators.Length(min=1, max=50)])
   # username = StringField('Username', [validators.Length(min=4, max=25)])
   # email = StringField('Email', [validators.Length(min=6, max=50)])
   # password = PasswordField('Password', [
   #     validators.DataRequired(),
   #     validators.EqualTo('confirm', message='Password do not match')
   # ])
    #confirm = PasswordField('Confirm Password')

#@app.route('/register', methods=['GET', 'POST'])
#def register():
#    form = RegistrationForm(request.formd)
 #   if request.method == 'POST' and form.validate():
   #     return render_template('register.html')  
    #return render_template('register.html', form=form) 


@app.route('/request', methods=['GET', 'POST'])

def request():
    return render_template('request.html')

@app.route('/diagnosecenter')
def diagnose():
    return render_template('diagnose.html')

@app.route('/news')
def news():
    return render_template('event.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sendmsg')
def sendmsg():
    return render_template('sendmsg.html')

@app.route('/wng')
def wng():
    return render_template('wng.html')

@app.route('/start')
def start():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)