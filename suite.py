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

filename = BASEDIR + '/report/waicl{}.html'.format(time.strftime('%Y%m%d%H%M%S'))

with open(filename,'wb')as d:
    run = HTMLTestRunner(d,verbosity=2,title='ihrm标题',description='ihrm内容')
    run.run(suite)








