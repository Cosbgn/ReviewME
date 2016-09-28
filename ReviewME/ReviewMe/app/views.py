from flask import render_template, redirect,request
from .forms import LoginForm

from app import app
#from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
	# need to get user information later
	user = {'nickname' : 'bakfunk'} 
	return render_template('index.html', title = 'Home',user=user)



@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	succeed = None
	form  = LoginForm()
	if form.validate_on_submit():
		succeed = "Login is succeed."
	return render_template('login.html',title='Login',error=error,succeed = succeed,form = form)