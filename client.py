import socket
import logging
logging.basicConfig(filename='socket1.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#creating a socket
c=socket.socket()
#connecting to server
c.connect(('localhost',9222))
#asking the client's name
name=input('enter your name')
#sending name to server
c.send(bytes(name,'utf-8'))
#receiving information from server and logging into file
logging.info(c.recv(1024))
#decoding the message and logging into file
logging.info(c.recv(1024).decode())