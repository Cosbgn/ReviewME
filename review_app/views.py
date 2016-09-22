#from flask import render_template
from flask import render_template, flash, redirect
from review_app import app
from .forms import LoginForm

@app.route('/')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('index.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/about')
def about():
    return render_template('about.html')
