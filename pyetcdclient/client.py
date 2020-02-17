#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2020-02-17 03:55
"""
import random
import time
import etcd3
from pyetcdclient.tools.utils import LOG
from multiprocessing.pool import ThreadPool
from concurrent.futures import ThreadPoolExecutor

class EtcdClient(object):
    def __init__(self, ServerList=("127.0.0.1:2379",), TLS=False, User=None, Password=None):
        self.serverlist = list()
        self.etcd_clientlist_length = 0
        for server in ServerList:
            if len(server.split(":")) == 2:
                self.serverlist.append(server)
        self.etcd_clientlist = list()
        self.tls_enable = TLS
        self._INIT()
        time.sleep(0.5)

    def SET_TLS(self):
        # TODO: If TLS Enable, Trigger this Function
        pass

    def GetTree(self, Depth=2):
        # TODO: Generate a Tree-like Data Structure
        try:
            etcd_client = self.RandomClientChoice()
            print(etcd_client)
        except Exception as expt:
            LOG.error("EtcdClient.GetTree Error - %s" % expt)

    ### System Code ###

    def _INIT(self):
        # TODO: Failover the ServerList by TimeOut Auto Dect

        if self.tls_enable is False:
            # Add the Callback-ThreadPool for Polling
            executor = ThreadPoolExecutor(max_workers=1)
            future = executor.submit(self._FailoverClient, self.serverlist)
            future.add_done_callback(lambda f: print(f.result()))
            executor.shutdown(False)  # non-blocking
        else:
            pass

    def RandomClientChoice(self):
        if self.etcd_clientlist_length > 0:
            return random.choice(self.etcd_clientlist)
        else:
            raise Exception("EtcdClient - No Sufficient Client List")

    def _FailoverClient(self, SERVERLIST):
        # TODO: Failover Algorithm Implementation

        def getstatus(client):
            try:
                status = client.status()
                LOG.debug("The client: <%s> version is %s" % (client,status.version))
                if status is not None:
                    return client
            except Exception as expt:
                LOG.error("The client: <%s> is broken" % client)
            return None

        while True:
            try:
                for etcd_client in self.etcd_clientlist:
                    if getstatus(etcd_client) is None:
                        self.etcd_clientlist.pop(etcd_client)
                if self.etcd_clientlist_length == len(self.etcd_clientlist) and self.etcd_clientlist_length != 0:
                    time.sleep(10)
                    continue
                with ThreadPool(3) as tp:
                    async_result = tp.map(getstatus,
                                      [etcd3.client(host=server.split(":")[0], port=server.split(":")[1], timeout=1) for
                                       server in SERVERLIST])
                self.etcd_clientlist = [etc for etc in async_result if etc is not None]
                self.etcd_clientlist_length = len(self.etcd_clientlist)
            except Exception as expt:
                LOG.error("EtcdClient.Client: Error Occur: %s" % expt)