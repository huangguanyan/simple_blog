# Simple blog.
一个简单的 Flask 蓝图小栗子，使用纯粹的 SQL 语句进行数据处理  

```
ProjectFolder:

  | README.md
  | run.py
  | piplist.txt
  | venv
  | src
  | - __init__.py
  | - config.py
  | - util.py
  | - app
  | - - __init__.py
  | - - welcome.py
```

```shell
pip install -r piplist.txt
```

需要注意的是，该项目下载后无法直接运行，因为里面包含了数据库的查询操作，而你本地没有对应的数据库和表
