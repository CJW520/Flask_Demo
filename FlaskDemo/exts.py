# MSI
# exts.py
# 时间：2024/4/27 下午9:26

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()


def ToJsonList(lists):
    return [models.to_json() for models in lists]

