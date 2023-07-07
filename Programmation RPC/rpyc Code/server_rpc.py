# encoding : utf-8
# author :Ibrahim Lahlou
# code : server_rpc.py

import rpyc
from rpyc.utils.server import ThreadedServer

class CalculService(rpyc.Service):
    def exposed_add(self,x,y):
        return x+y
    def exposed_mul(self,x,y):
        return x*y


server = ThreadedServer(CalculService,hostname="8.8.8.8",port=7000)
server.start()