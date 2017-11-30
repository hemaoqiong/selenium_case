# coding=utf-8
import os
import logging
import time


class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
    # 定义日志保存位置
        # filepath = os.path.abspath('.')
        # filepath=os.path.dirname(os.path.abspath('.'))
        filepath = os.path.abspath('.')
        filepath2 = os.path.join(filepath, 'logs')
        now = time.strftime('%Y-%m-%d  %H%M%S', time.localtime())

        filename = filepath2 + '/' + now + '.log'
    # 定义文件输入和控制台输出日志
        ch = logging.FileHandler(filename, mode='a')
        sh = logging.StreamHandler()
    # 定义handler的输出格式
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(filename)s - [line:%(lineno)d]-%(levelname)s:%(message)s')
    # 设置输出格式
        ch.setFormatter(formatter)
        sh.setFormatter(formatter)
    # 给logger添加handler
        self.logger.addHandler(ch)
        self.logger.addHandler(sh)

    def info(self, msg):
        self.logger.info(msg)


# if __name__ == '__main__':
#     log = Logger()
#     log.info('this is a info good thing.')

'''可运行的log'''

# import logging
# import os


# class Logger:
#     def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
#         self.logger = logging.getLogger(path)
#         self.logger.setLevel(logging.DEBUG)
#         fmt = logging.Formatter(
#             '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
#         # 设置CMD日志
#         sh = logging.StreamHandler()
#         sh.setFormatter(fmt)
#         sh.setLevel(clevel)
#         # 设置文件日志
#         fh = logging.FileHandler(path)
#         fh.setFormatter(fmt)
#         fh.setLevel(Flevel)
#         self.logger.addHandler(sh)
#         self.logger.addHandler(fh)

#     def debug(self, message):
#         self.logger.debug(message)

#     def info(self, message):
#         self.logger.info(message)

#     def war(self, message):
#         self.logger.warn(message)

#     def error(self, message):
#         self.logger.error(message)

#     def cri(self, message):
#         self.logger.critical(message)


# if __name__ == '__main__':
#     # 定义日志保存位置
#         # filepath = os.path.abspath('.')
#         # filepath=os.path.dirname(os.path.abspath('.'))
#     filepath = os.path.abspath('..')
#     filepath2 = os.path.join(filepath, 'logs')
#     now = time.strftime('%Y-%m-%d  %H%M%S', time.localtime())

#     filename = filepath2 + '/' + now + '.log'

#     logyyx = Logger(filename, logging.INFO, logging.DEBUG)
#     logyyx.debug('一个debug信息')
#     logyyx.info('一个info信息')
#     logyyx.war('一个warning信息')
#     logyyx.error('一个error信息')
#     logyyx.cri('一个致命critical信息')
