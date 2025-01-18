from flask import Blueprint, render_template
from flask_security import auth_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html') 

@main.route('/community')
@auth_required()
def community():
    return render_template('community.html')

@main.route('/charity')
def charity():
    return render_template('charity.html')

@main.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')