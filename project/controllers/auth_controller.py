from flask import Blueprint, render_template, request, redirect, url_for, session
from models.models import db, User, Admin

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/')
def home():
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin':
            admin = Admin.query.filter_by(username=username, password=password).first()
            if admin:
                session['admin'] = True
                return redirect(url_for('admin.dashboard'))
        else:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['user_id'] = user.id
                return redirect(url_for('user.dashboard'))
        return "Invalid Credentials"
    return render_template('login.html')

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')

