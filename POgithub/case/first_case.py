import os
import sys

BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BATH_PATH)
import time
import unittest
import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is chrome")
        self.login = RegisterBusiness(self.driver)
        self.file_name = os.path.join(BATH_PATH, 'image', 'test001.png')

    def tearDown(self) -> None:
        time.sleep(2)
        # 捕获程序是否有异常，有则截图保存
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(BATH_PATH, 'report', case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.close_handle()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34', 'user111', '11111', self.file_name)
        return self.assertFalse(email_error, "测试失败")

    def test_login_username_error(self):
        username_error = self.login.login_name_error('12123@qq.com', 't1', '111111', self.file_name)
        self.assertTrue(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_code_error('11121@qq.com', 'ss22212', '111111', self.file_name)
        self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.login.login_password_error('11311@qq.com', 'ss23222', '111111', self.file_name)
        self.assertFalse(password_error)

    def test_login_success(self):
        # success = self.login.register_success('12221@qq.com', '23213', '111111', self.file_name)  # 成功
        success = self.login.register_success('12221', '2321', '111111', self.file_name)  # 失败
        # print(success)
        self.assertTrue(success)


"""
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
"""

if __name__ == '__main__':
    # unittest.main()
    file_path = os.path.join(BATH_PATH, 'report', 'first_case.html')  # F:\Pycharm\muke\POpractice\report\first
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_email_error'))
    # suite.addTest(FirstCase('test_login_username_error'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title="This is first123 report",
                                           description=u"这个是我们第一次测试报告",
                                           verbosity=2)
    runner.run(suite)
    f.close()
