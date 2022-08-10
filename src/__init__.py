from flask import Flask
from flas_sqlalchemy import SQLAlchemy
from src.util import standard_result
import src.config as config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)


def run():
    
    # 蓝图注册
    from .app import welcome
    app.register_blueprint(welcome.bp)
    
    
    # debug 在部署到生成环境时记得关掉哇
    app.run(debug=True)
