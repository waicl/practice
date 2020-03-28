# 套件
import time
import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner

from app import BASE_DIR
from script.login_test import LoginSuccess
from script.test_login import TestIHRMLogin
from utils import BASEDIR

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LoginSuccess))

# filename = BASEDIR + '/report/waicl{}.html'.format(time.strftime('%Y%m%d%H%M%S'))
filename = BASEDIR + '/report/waicl.html'

with open(filename,'wb')as d:
    run = HTMLTestRunner(d,verbosity=2,title='ihrm标题',description='ihrm内容')
    run.run(suite)

print('更改输出语句,然后查看是否会自动触发轮循构建，最长不会超过一分钟')







