#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2020-02-17 04:01
"""
class Node(object):
    def __init__(self,Directory,Key,Value):
        #TODO: Info to Element
        self.Directory = Directory
        self.Value = Value
        pass

    def get_directory(self):
        return self.Directory

    def get_value(self):
        return self.Value
