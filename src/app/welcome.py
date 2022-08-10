from flask import Blueprint
from src import db
from src.util import serialize_sql_result, standard_result

bp = Blueprint('Welcome', __name__)

@bp.route("/")
def welcome_get_user():
  
  '''
  值得注意的是，如果是通过接收参数作为条件筛选，必须要对参数值进行处理，以免不法分子能随意在你的博客获取到数据
  总不能一个简单的 select * from user where (nickName='1' OR '1'='1') 就把用户全暴露了吧
  '''
  user_query = db.session.execute("select nickName,headPortrait,createdTime from user")
  result = user_query.fetchall()
  
  return standard_result(200, serialize_sql_result(result))
