import configparser


# cf = configparser.ConfigParser()
# cf.read('F:\Pycharm\muke\POpractice\config\LocalElement.ini')
# print(cf.get('RegisterElement','user_email'))

class ReadIni:

    def __init__(self, node=None, file_name=None):
        if file_name == None:
            file_name = r'F:\Pycharm\muke\POpractice\config\LocalElement.ini'
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载文件。
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取值。
    def get_value(self, key):
        data = self.cf.get(self.node,key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('user_name'))