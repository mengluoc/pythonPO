import time
from PIL import Image
from ShowapiRequest import ShowapiRequest


class GetCode:
    def __init__(self, driver):
        self.driver = driver

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "189692", "970559aaeb784556a483448edd3b5482")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text
