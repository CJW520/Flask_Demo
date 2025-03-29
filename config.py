# MSI
# Config.py
# 时间：2024/4/25 下午10:28

# MySQL所在的主机名
HOSTNAME = "192.168.2.100"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，读者用自己设置的
USERNAME = "LIS"
# 连接MySQL的密码，读者用自己的
PASSWORD = "LIS"
# MySQL上创建的数据库名称
DATABASE = "test"
# 连接MySQL的URL
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False

HOST = '0.0.0.0'
DEBUG = True

# 邮箱配置
# 发送邮件服务器： smtp.qq.com，使用SSL，端口号465或587
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "1427628179@qq.com"
MAIL_PASSWORD = "wzzgvsydjnsjbabd"
MAIL_DEFAULT_SENDER = "1427628179@qq.com"