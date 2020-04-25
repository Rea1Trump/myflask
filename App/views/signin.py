from flask import Blueprint
from flask import request, render_template
from App.models.models import db, User

signin = Blueprint('signin', __name__)


@signin.route('/')
def index():

    return render_template('index.html', title='Index')


@signin.route('/signin/', methods=['POST', 'GET'])
def signinpage():
    if request.method == 'POST':
        user = request.form

        if User.query.filter(user):
            return '登陆成功'
        else:
            return 'bad'
    else:
        return render_template('signin.html', title='Sign in')
