#-*- coding:utf-8 -*-
'''
created by YHR   2016-11-2
Read File
'''
__version__ = '0.1'

class ReadFile(object):
    def __init__(self):
        pass
    def Read_File(self,FilePath):
        f = open(FilePath)
        text = f.read()
        return text
        f = close(FilePath)
