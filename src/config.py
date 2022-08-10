'''
这里我要使用的是 mysql 数据库，由于 sqlalchemy 默认连接的是 sqllite3 数据库，因此要做出改变
'''

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset={charset}".format(
    user = 'root',
    password = 'roow',
    host = 'localhost',
    port = 3306,
    db = 'blog',
    charset = 'utf8'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
