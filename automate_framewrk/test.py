# coding=utf-8

import os
import time
# from package.common.logger import Logger

# logger = Logger(logger="paht")
# logger = Logger(logger="BasePage").getlog()


def main():
    path = os.path.abspath('.')
    path1 = os.path.join(path, "package")
    print"os.path.abspath('.') is:"
    print (path)
    print path1
    # logger.info("os.path.abspath('.') is:" % path)
    dpath = os.path.dirname(path)
    print "os.path.dirname(path) is:"
    print (dpath)
    now = time.strftime('%Y-%m-%d   %H:%M', time.localtime())
    filepath = os.path.dirname(path) + now + '.logs'
    print filepath
    filepath1 = path1 + now + ".logs"


if __name__ == '__main__':
    main()
