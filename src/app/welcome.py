from flask import Blueprint
from src import db
from src.util import serialize_sql_result, standard_result

bp = Blueprint('Welcome', __name__)

@bp.route("/")
def welcome_get_user():
  

  # 获取昵称中包含 test 字符的所有用户
  user_query = db.session.execute("select * from user where regexp_like(nickName, '%s')" % ("test",))
  result = user_query.fetchall()
  
  return standard_result(200, serialize_sql_result(result))
