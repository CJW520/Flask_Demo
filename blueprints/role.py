# MSI
# role.py
# 时间：2024/4/27 下午4:40
from flask import Blueprint, jsonify

from exts import db, ToJsonList
from model import Role

role_bp = Blueprint('role', __name__, url_prefix='/role')


@role_bp.route('/list',methods=['GET','POST'])
def role_list():
    db
    role = Role.query.filter().all()
    if len(role) > 0:
        data = {'code': 0, 'msg': '获取成功', 'data': ToJsonList(role)}
    else:
        data = {'code': 1, 'msg': '获取失败', 'data': None}
    # print(data)
    return jsonify(data)


@role_bp.route('/add')
def role_add():
    return 'role add'


@role_bp.route('/edit')
def role_edit():
    return 'role edit'


@role_bp.route('/delete')
def role_delete():
    return 'role delete'


@role_bp.route('/rolec')
def rolecreate():

    role1 = Role(name='超级管理员')
    role2 = Role(name='管理员')
    role3 = Role(name='副总管理')
    role4 = Role(name='副管理')
    db.session.add_all([role1, role2, role3, role4])
    db.session.commit()
    return 'ok'
