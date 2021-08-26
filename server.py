import socket
import logging
logging.basicConfig(filename='socket1.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#creating a socket
s=socket.socket()
#logging the info into file.
logging.info('Socket Created')
#binding with a port
s.bind(('localhost',9222))
#assigning the maximum listening capacity of the server
s.listen(3)
#logging into file
logging.info('Waiting for connections')
while True:
    #accepting the client requests
    c,add=s.accept()
    #receiving name from client
    name=c.recv(1024).decode()
    #logging the connection info
    logging.info('Connected with:{} name is {}'.format(add,name))
    #send a message to the client in the format of bytes with utf-8 format
    c.send(bytes('Hi, This is the sample program. My name is sindhu.','utf-8'))
    #close the connection
    c.close()

