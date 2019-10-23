from flask import Blueprint
from . import views
from flask import render_template
from . import auth

auth = Blueprint('auth',__name__)




@auth.route('/login')
def login():
    return render_template('auth/login.html')
