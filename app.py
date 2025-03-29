# MSI
# app.py
# 时间：2024/4/25 下午8:58

from model import User, Role
from exts import db, mail, ToJsonList
from flask import Flask, jsonify, request, render_template, redirect, session, url_for
from blueprints.role import role_bp
from blueprints.user import user_bp
from flask_migrate import Migrate
from flask_mail import Message
import config
app = Flask(__name__)
# region  加载配置
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
app.register_blueprint(role_bp, url_prefix='/role')
app.register_blueprint(user_bp, url_prefix='/user')
app.secret_key = 'cjw74520'
migrate = Migrate(app, db)

# endregion

# memcached/redis
# 可不登录情况下直接访问的页面
urls = ['login', 'login1', 'login2', 'login3', 'login4', 'login5']

# 发送邮件
# @app.route('/')
# def hello_world():
#     msg = Message(subject='测试邮件', recipients=['161870163@qq.com'], body='Flask测试邮件')
#     mail.send(msg)
#     session['User'] = {'name': 'admin'}
#     return 'Hello, World!'


# @app.route('/login')
# def login():
#     return 'login!'
# @app.route('/login1')
# def login1():
#     return 'login1!'
# @app.route('/login2')
# def login2():
#     return 'login2!'
# @app.route('/login3')
# def login3():
#     return 'login3!'
# @app.route('/login4')
# def login4():
#     return 'login4!'


@app.before_request
def before_request():
    user = session.get('User')
    print('User' not in session)
    print(request.endpoint not in urls)

    if 'User' not in session and request.endpoint not in urls:
        print('进入登录页')
        return redirect(url_for('login'))
        # hello_worlds()
    if 'User' in session:
        print('获取到session')
        print(session['User']['name'])
    print('before request')


@app.after_request
def after_request(response):
    return response


@app.route('/1')
def hello_worlds():
    roles = Role.query.filter().all()
    for r in roles:
        print(r.name)
        print(len(r.users.all()))
        # for u in r.users.all():
        print(ToJsonList(r.users.all()))
    return 'page1!'


@app.route('/login1')
def login1():  # 登录页面
    return 'login1登录页面!<br><a href="/1">登录完成</a>'


@app.route('/login2')
def login2():  # 登录页面
    return 'login2登录页面!<br><a href="/1">登录完成</a>'


@app.route('/login3')
def login3():  # 登录页面
    return 'login3登录页面!<br><a href="/1">登录完成</a>'


@app.route('/login4')
def login4():  # 登录页面
    return 'login4登录页面!<br><a href="/1">登录完成</a>'


@app.route('/login5')
def login5():  # 登录页面
    return 'login5登录页面!<br><a href="/1">登录完成</a>'


@app.route('/login')
def login():  # 登录页面

    session['User'] = {'name': 'admin'}
    print(session['User'])
    return '登录页面!<br><a href="/1">登录完成</a>'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    # flask run  -- host 0.0.0.0 --port 6666 --debug

# flask db init
# flask db migrate
# flask db upgrade
