#导包
import unittest
import requests

import data
from api.login_api import LoginApi
from parameterized import parameterized

from app import BASE_DIR
from utils import read_login_data


# 创建测试类
class TestIHRMLogin(unittest.TestCase):

    # 进行初始化
    def setUp(self) -> None:
        self.login_api = LoginApi()
    def tearDown(self) -> None:
        pass

    # 创建测试方法

    filename = BASE_DIR + '/data/login.json'
    @parameterized.expand(read_login_data(filename=filename))
    def test01_login(self,mobile,password,success,code):
        #使用requests模块发送登录接口请求
        response = self.login_api.login(mobile,password)
        # 打印登录结果
        print('登录结果为:',response.json())
        # 对登录结果进行断言
        self.assertEqual(success,response.json().get('success'))
        self.assertEqual(code,response.json().get('code'))


















