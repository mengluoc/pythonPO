#coding=utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement
from ShowapiRequest import ShowapiRequest


class RegisterFunction():

    def __init__(self,url):
        self.driver = self.get_driver(url)

    # 获取driver并且打开url
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息。
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 生成随机数。
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefg', 8))
        return user_info

    # 获取图片。
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)  # 截屏。
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))  # 截取验证码
        img.save(file_name)

    # 识别验证码。
    def code_online(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)
        # img需改为image，文件上传时设置
        res = r.post()
        print(res.text)
        # text = res.json()['showapi_res_body']['Result']
        return 1111

    def run_main(self):
        user_info = self.get_range_user()
        user_email = user_info + '@163.com'
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_info)
        self.send_user_info('password', 111111)
        self.send_user_info('code_text', self.code_online(r'F:\Pycharm\muke\POpractice\practice\imooc1.png'))
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    register = RegisterFunction('http://www.5itest.cn/register')
    register.run_main()