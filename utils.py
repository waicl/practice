# 存放自定义开发的工具类
import json
import os


#json读取数据方法
#讲师封装在了utlis中
def read_login_data(filename):
    with open(filename,'r',encoding='utf8')as d:
        # 把数据加载成json格式
        python_file = json.load(d)
        # 先定义一个存储数据的空列表
        result = []
        for n in python_file:
            print(n)
            mobile = n.get("mobile")
            password = n.get("password")
            success = n.get('success')
            code = n.get('code')
        # list_file = list(python_file)
            result.append((mobile,password,success,code))
            print(result)
        return result


# 封装基目录

BASEDIR = os.path.dirname(os.path.abspath(__file__))






if __name__ == '__main__':
    # 编写调试读取登录数据的函数
    read_login_data('./data/login.json')



