from cryptography.fernet import Fernet
import socket
import logging
logging.basicConfig(filename='ClientDecrypt.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#creating a socket
c=socket.socket()
#connecting to server
c.connect(('localhost',9222))
#asking the client's name
name=input('enter your name')
#sending name to server
c.send(bytes(name,'utf-8'))
#receiving information from server and logging into file
enc=c.recv(1024)
#logging the received encrypted information
logging.info('The encrypted message received is {}'.format(enc))
# Open the file to read the key
file=open('ServerEncrypt.key','rb')
key=file.read()
#closing the file
file.close()
#logging the key
logging.info('The key using for decryption is {}'.format(key))
f1=Fernet(key)
#decrypting the message
try:
    dec=f1.decrypt(enc)
    logging.info("Valid Key - Successfully decrypted")
    #logging the decrypted message
    logging.info('The decrypted message is {}'.format(dec))
except:
    logging.info("Invalid Key - Unsuccessfully decrypted")
