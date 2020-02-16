#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: zzetian@cn.ibm.com
@software: PyCharm
@time: 2020-02-17 03:55
"""
import etcd3

class EtcdClient(object):
    def __init__(self, ServerList=("127.0.0.1:2379",),TLS=False,User=None,Password=None):
        self.serverllist = ServerList
        self._INIT()

    def SET_TLS(self):
        #TODO: If TLS Enable, Trigger this Function
        pass

    def _INIT(self):
        #TODO: Failover the ServerList by TimeOut Auto Dect
        pass