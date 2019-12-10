from flask import Flask, flash, redirect, render_template, request, session, abort
import pprint
import time
import datetime
#from flask_login import LoginManager, UserMixin

from DataAccess import DataAccess
from CityService import CityService


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import url_for



app = Flask(__name__)

db = SQLAlchemy(app)
#migrate = Migrate(app, db)
db.create_all()
#login_manager = LoginManager()
#login_manager.init_app(app)

#class User(UserMixin,db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(30), unique=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/logged_in', methods=['POST'])

def my_index_post():
    text = request.form['text']
    date_picked = request.form['date_picked']
    print("DATEPICKED: "+date_picked+"       ")
    #pprint(date_picked)
    processed_text = text.upper()
    #today = datetime.datetime.now()
    results_list = DataAccess(processed_text,date_picked)
    service_list =[]
    
    for items in results_list:
        result = []
        insert_return = "\n"
        for item in items.items():
            result.append(item[1])
            print(item[0])        
        cservice = CityService(result)
        service_list.append(cservice)  
        print(cservice.SERVICE_NAME)  
    if(len(results_list) == 0):
        empty_list=[]
        return render_template('logged_in.html',M_List=empty_list)


    return render_template('logged_in.html',S_List=service_list)


@app.route('/home',methods=['GET','POST'])
def home():
    if request.method =='POST':
        validate()
    
    return render_template('home.html')

@app.route('/join',methods=['GET','POST'])
def join():
    if request.method == 'POST':
        return redirect(url_for('logged_in'))
    return render_template('join.html')

def validate():
    username = request.form['username']
    pw = request.form['pw']
    pver = ''#request.form['pver']
    email = ''#request.form['email']

    username_error = ''
    pw_error = ''  
    pver_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter a valid username'
    elif len(username) < 3 or len(username) > 20 or " " in username:
        username_error = 'Username must contain between 3 and 20 characters and cannot contain spaces.'
        
    if pw == '':
        pw_error = 'Please enter a valid password'
    elif len(pw) < 3 or len(pw) > 20 or " " in pw:
        pw_error = 'Password must contain between 3 and 20 characters and cannot contain spaces.'

    if pw != pver:
        pver_error = 'Password does not match.'
        
    if email != '':
        if len(email) < 3 or len(email) > 20 or " " in email or "@" not in email or "." not in email:
            email_error = "Please enter a valid email address."

    if not username_error and not pw_error and not pver_error and not email_error:
        return redirect(url_for('logged_in'))
    else:
        return render_template('home.html', username_error = username_error, pw_error = pw_error, 
            pver_error = pver_error, email_error = email_error, username = username, email = email)
@app.route('/logged_in')
def logged_in():
    
    return render_template('logged_in.html')




if __name__ == "__main__":
    app.run(debug=True)