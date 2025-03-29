# MSI
# user.py
# 时间：2024/4/27 下午4:40

from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import func

from exts import db, ToJsonList
from model import User

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    return 'User Page'


@user_bp.route('/login')
def login():
    return 'User Login Page'


@user_bp.route('/logout')
def logout():
    return 'User Logout Page'


@user_bp.route('/register')
def register():
    return 'User Register Page'


@user_bp.route('/profile')
def profile():
    return 'User Profile Page'


@user_bp.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        role = request.form.get('role')
        print('id：' + id + '    name：' + name + '    age：' + age + '    sex：' + sex + '    role：' + role)
        if id == '' or id is None:
            user = User(name=name, age=age, sex=sex, role_id=role)
            db.session.add(user)
        else:
            User.query.filter_by(id=id).update({'name': name, 'age': age, 'sex': sex, 'role_id': role})
        db.session.commit()
        return redirect('/user')
    else:
        id = request.args.get('id')
        if id:
            user = User.query.filter_by(id=id).first()
            user = user.to_json()
            user['type'] = 'edit'
            if user:
                data = {'code': 0, 'msg': '查询成功', 'data': user}
            else:
                data = {'code': 1, 'msg': '查询失败', 'data': None}
        else:
            data = {'code': 1, 'msg': '查询失败', 'data': None}
        return render_template('2.html', data=data)


@user_bp.route('/delete', methods=['POST'])
def delete():
    id = request.get_json().get('id')
    user = User.query.filter_by(id=id)
    if user.first():
        print('删除用户：', ToJsonList(user.all()))

        user.delete()
        db.session.commit()
        data = {'code': 0, 'msg': '删除成功', 'data': None}
    else:
        data = {'code': 1, 'msg': '删除失败', 'data': None}
    return jsonify(data)


@user_bp.route('/delbyid', methods=['POST'])
def delbyid():
    ids = request.get_json().get('id')
    ids = [int(i) for i in ids]
    user = User.query.filter(User.id.in_(ids))
    if user.first():
        print('删除用户：', ToJsonList(user.all()))
        user.delete()
        db.session.commit()
        data = {'code': 0, 'msg': '删除成功', 'data': None}
    else:
        data = {'code': 1, 'msg': '删除失败', 'data': None}
    return jsonify(data)


@user_bp.route('/edit')
def edit():
    return 'User Edit Page'


@user_bp.route('/list')
def user_list():
    user = User.query.order_by(User.role_id.asc()).all()
    d=ToJsonList(user)

    # for u in user:
    #     print(u.to_json())
    return render_template('1.html',data=d)

@user_bp.route('/lists')
def user_lists():
    user = User.query.order_by(User.role_id.asc()).all()
    d=ToJsonList(user)



    result = User.query.with_entities( User.role_id, func.count(User.id)).group_by(User.role_id).all()
    print(  result)
    # for u in user:
    #     print(u.to_json())
    return ToJsonList(result)


