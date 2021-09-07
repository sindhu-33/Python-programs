import socket
import logging
from cryptography.fernet import Fernet
logging.basicConfig(filename='ServerEncrypt.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
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
    #generating key to encrypt the string
    key = Fernet.generate_key()
    # logging the key
    logging.info('Generated key is {}'.format(key))
    #Open the file as wb to write bytes
    file=open('ServerEncrypt.key','wb')
    #write the key into file
    file.write(key)
    #close the file
    file.close()
    msg="My name is sindhu".encode()
    #logging the enncoded msg
    logging.info('The message passing to the client is {}'.format(msg))
    f = Fernet(key)
    #encypting the message
    enc = f.encrypt(msg)
    #logging the encrypted message
    logging.info('the encrypted message is {}'.format(enc))
    #sending the encrypted message to the client
    c.send(enc)
    #close the connection
    c.close()

