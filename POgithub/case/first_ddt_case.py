import os
import sys

BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BATH_PATH)

import time
import ddt
import unittest
import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness
from utils.excel_util import ExcelUtil

file_name = os.path.join(BATH_PATH, 'image', 'test001.png')
ex = ExcelUtil()
data = ex.get_data()


@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        # 捕获程序是否有异常，有则截图保存
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(BATH_PATH, 'report', case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @ddt.data(*data)
    @ddt.unpack
    def test_register_case(self, *data):
        email, username, password, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, file_name, assertCode, assertText)
        self.assertFalse(email_error, "测试失败")


if __name__ == '__main__':
    file_path = os.path.join(BATH_PATH, 'report', 'first_case1.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description=u"这个是第一次测试报告1",
                                           verbosity=2)
    runner.run(suite)
    f.close()
