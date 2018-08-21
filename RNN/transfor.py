# -*-coding:utf-8-*-
"""
@Time   : 2018/8/21 16:37
@Author : Mark
@File   : transfor.py
"""
import io
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Transfor(object):
    def __init__(self):
        pass

    def process(self, input_file, output_file):
        with open(input_file) as f:
            for l in f.xreadlines():
                words = l.split(u' ')
                for word in words:
                    self.write_file(word)

    def write_file(self, content_text):
        try:
            file_obj = io.open(output_file, mode=u"a", encoding=u"utf-8")
            file_obj.write(content_text + u"\n")
            file_obj.close()
        except Exception as e:
            logging.exception(u'write file error {0}'.format(str(e)))


if __name__ == u'__main__':
    input_file = u'./金庸.txt'
    output_file = u'./input.txt'
    Transfor().process(input_file, output_file)
