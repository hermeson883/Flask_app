from app import app, db
from flask import render_template, flash
from flask_login import login_user
from app.models.table import User
from app.models.forms import LoginForm

@app.route("/index/<user>")
@app.route("/", defaults={'user':None})
def index(user):
    return render_template('index.html',
                           user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:
                login_user(user)
                flash('Logado!')
            else:
                flash('Invalid loggin.')
    else:
        print(form.errors)
    return render_template('login.html',
                           form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User("hermeson", "1234", "hermeson beserra", "hermeson@gmail.com")
    db.session.add(r)
    db.session.commit()
