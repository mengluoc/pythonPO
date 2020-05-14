import os
import logging
import datetime
BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
log_file = os.path.join(BATH_PATH, 'log', 'logs', file_name)


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()        # 创建一个logger
        self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_file)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s %(module)s %(levelno)s %(levelname)s %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        # logger.debug('reee')

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()