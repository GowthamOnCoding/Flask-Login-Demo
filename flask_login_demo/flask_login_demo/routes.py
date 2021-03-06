from flask_login_demo import app,db,login_manager
from flask import render_template,flash,redirect,url_for
from .forms import LoginForm, RegistrationForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user,login_required,current_user

@app.route('/')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        print(user)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('dashboard'))
    return render_template('login.html',form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    app.logger.debug("Entering inside signup")
    form = RegistrationForm()
    print(form.username.data,form.email.data,form.password.data)  
    if form.validate_on_submit():
        hashed_pwd = generate_password_hash(form.password.data,method='sha256')
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        return "Registered successfully"
    else:
        print('not validated')
    return render_template('signup.html',form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

