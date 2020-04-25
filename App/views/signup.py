from flask import Blueprint, request, render_template
from App.models.models import db, User

signup = Blueprint('signup', __name__)


@signup.route('/signup/', methods=['POST', 'GET'])
def signinpage():
    user = User()
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        db.session.add(user)  # 04-25//user是类，如果想要插入一组等价的数据那么可以把所有类组成一个字典，插入一个字典
        db.session.commit()  # 04-25//也不知道commit是不是每次都要，还是可以add所有之后一次commit，没实验过
        return '注册成功'
    else:
        db.create_all()
        return render_template('signup.html',title='Signup')
