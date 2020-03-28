import json
import unittest

from api import api_login
from api.api_login import LoginApi
from parameterized import parameterized

#定义读取json数据的方法
from utils import BASEDIR


def read_login_data(filename):
    with open(filename,'r',encoding='utf8')as d:
        result = []
        python_file = json.load(d)
        for n in python_file:
            mobile = n.get("mobile")
            password = n.get("password")
            success = n.get("success")
            code = n.get("code")
            message = n.get("message")
        result.append((mobile,password,success,code,message))

        return result



class LoginSuccess(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = LoginApi()
    def tearDown(self) -> None:
        pass


    @parameterized.expand(read_login_data(BASEDIR + '/data/login.json'))
    def test01_login(self,mobile,password,success,code,message):
        response = self.login_api.login(mobile,password)
        self.assertEqual(success,response.json().get("success"))
        self.assertEqual(code,response.json().get("code"))
        self.assertIn(message,response.json().get("message"))





















