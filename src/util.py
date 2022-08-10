'''
一些处理数据的公共函数抽取出来可以做成一个工具
比如说数据库查询出来的结果并不是我们所需要的数据类型或格式时，就可以使用工具处理
不至于一个同样功能的函数遍布各个蓝图，虽然这个函数可能就三四行代码
'''
import datetime
import json

'''
想要对数据库查询出来的结果进行 json 化返回，一定要对 json 进行扩展
例如下面这个扩展，如果不对 datetime 进行处理，在进行 json.dumps(result) 时就会报错
'''

# 版权声明
# class DateEncoder 的代码来源
# https://blog.csdn.net/t8116189520/article/details/88657533
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%M-%D %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)
        pass
    pass
# 声明结束


'''
使用 sqlalchemy.session.execute(sql) 获取到的数据格式并非我们所设想的那样
设想: [{ [key]: [value] }]
现实: [( value, value )]

那么应该如何解决这个问题？
将返回的数据集 列表[元组,元组] 转换成 列表[字典,字典] 即可

返回的结果中虽然显示是 list(tuple)，但那也只是显示，实际上 tuple 背后带上了对应的字典类型数据 (想不明白是怎么实现的)
'''
def serialize_sql_result(data):
    result = []
    for row in data:
        dic = {}
        # print(row) 显示出来的是元组，但又可以使用字典的内置方法 .keys() 获取键，怎么做到的呢？
        for key in row.keys():
            dic.setdefault(key, row[key])
            pass
        
        result.append(dic)
        pass
    return json.dumps(result, cls=DateEncoder)



'''
标准化结构结果返回
有兴趣的可以进行改造，比如对 code 进行限制，不能虽然什么 123 都能传进来
'''
def standard_result(code, res, msg = ''):
    return {
        "code": code,
        "data": json.loads(res),
        "msg": msg
    }
