# MSI
# model.py
# 时间：2024/4/25 下午10:18

from exts import db


class Role(db.Model):
    # 定义模型类
    __tablename__ = 'lis_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False, comment='角色名称')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class User(db.Model):
    # 定义模型类
    __tablename__ = 'lis_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False, comment='姓名')
    age = db.Column(db.Integer, nullable=False, comment='年龄')
    sex = db.Column(db.Integer, nullable=False, comment='性别')
    role_id = db.Column(db.Integer, db.ForeignKey('lis_role.id'), comment='角色id')
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))
    birthday = db.Column(db.Date, nullable=False, comment='出生日期')

    def to_json(self):
        sex = ''
        if self.sex == 1:
            sex = '男'
        elif self.sex == 2:
            sex = '女'
        else:
            sex = '未知'
        return {'id': self.id,
                'name': self.name,
                'age': self.age,
                'sex': self.sex,
                'sex_name': sex,
                'role': self.role.name,
                'role_id': self.role_id}


class Dtmtxmtemplate(db.Model):
    __tablename__ = 'dtm_txmtemplate'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_type = db.Column(db.String(200), nullable=False, comment='患者类型')
    txm_template = db.Column(db.Text, nullable=False, comment='模板内容')
    hospital_id = db.Column(db.String(200), nullable=False, comment='医院id')
    # photo = db.Column(db.String(200), nullable=True, comment='照片')
    # photos = db.Column(db.LargeBinary, nullable=True, comment='照片')
    photos = db.Column(db.BLOB, nullable=True, comment='照片')

    def to_json(self):
        return {
            'id': self.id,
            'patienttype': self.patienttype,
            'txmtemplate': self.txmtemplate,
            'hospitalid': self.hospitalid
        }
