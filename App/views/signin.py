from flask import Blueprint
from flask import request, render_template
from App.models.models import db, User

signin = Blueprint('signin', __name__)


@signin.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    #


@signin.route('/signin/', methods=['POST', 'GET'])
def signinpage():
    user = User()
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        db.session.add(user)
        db.session.commit()
        return 'ok'
    else:
        db.create_all()
        return render_template('signin.html')
