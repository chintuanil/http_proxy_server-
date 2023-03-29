from socket import*
from acessingfiles import *
from reqparsing import *
import requests as req

class Proxyserver:
    def __init__(self,port):
        self.ip="0.0.0.0"
        self.port=port
        self.socket = socket(AF_INET ,SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.socket.bind((self.ip , self.port))
        self.acessingfiles=acessingfiles()
        self.isvalid=True
    def listen(self,waiters):
        self.socket.listen(waiters)
        print("your server is runnung",self.port)

    def accept(self):
        self.clientresponse , self.address=self.socket.accept()
        self.request=self.clientresponse.recv(1024).decode()
        print(self.request)
        reqparser = reqparsing(self.request)
        self.method=reqparser.reqmethods()
        self.url=reqparser.requrls()
        self.host=reqparser.reqhosts()
        self.checkingblocked(self.host)
        self.blockedkeywords(self.host)
        self.forwardresponse()
    def checkingblocked(self,hostname):
        list1=["test.com","king.com","wastematter.com"]
        if(hostname in list1):
            self.isvalid=False
            message=self.acessingfiles.acessfile2()
            self.clientresponse.sendall(message.encode('utf-8'))
            self.clientresponse.close()


    def blockedkeywords(self,keywords):
        list2=["movies","waste","bad","ugly","useless"]
        if(str(keywords)  in list2):
            self.isvalid=False
            message=self.acessingfiles.acessfile3()
            self.clientresponse.sendall(message.encode('utf-8'))
            self.clientresponse.close()

    def forwardresponse(self):
        if(self.isvalid==True):
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12;rv: 55.0) Gecko / 20100101Firefox / 55.0', }
            requesting=req.get(url=self.url,headers=headers)
            self.clientresponse.sendall(requesting.content)



while True:
    obj1=Proxyserver(1067)
    obj1.listen(10)
    obj1.accept()













