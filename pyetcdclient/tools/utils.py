#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2020-02-17 04:12
"""

import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%b-%d %H:%M:%S',
                        level=logging.DEBUG)

class LOG(object):
    @staticmethod
    def success(value):
        logging.info(value)

    @staticmethod
    def warn(value):
        logging.warning(value)

    @staticmethod
    def debug(value):
        logging.debug(value)

    @staticmethod
    def error(value):
        logging.error(value)