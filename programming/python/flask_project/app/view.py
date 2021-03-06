from flask import render_template, flash, redirect, url_for
from app import app, db
from forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app import User


@app.route('/')
def index():
    user = current_user
    if current_user.is_anonymous:
        user = 'незнакомка'
        return render_template('index.html', user=user)
    return render_template('index.html', user=user.username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный пароль или имя пользователя')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
# @login_required
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.mail.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляем, вы успешно зарегистрированы')
        return redirect(url_for('login'))
    return render_template('/register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
