import socket
import logging
import string
a=string.ascii_lowercase+string.ascii_lowercase
logging.basicConfig(filename='ServerCipher.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#creating a socket
c=socket.socket()
#connecting to server
c.connect(('localhost',9223))
#asking the client's name
name=input('enter your name\n')
#sending name to server
c.send(bytes(name,'utf-8'))
#receiving information from server and logging into file
s=c.recv(1024).decode()
#logging the received encrypted information
logging.info('The encrypted message received is {}'.format(s))
# Open the file to read the key
file=open('ServerEncrypt.key','r')
sn=int(file.read())
#closing the file
file.close()
#logging the key
logging.info('The shift number using for decryption is {}'.format(sn))
#decrypting the message
s=list(s)
for i in range(len(s)):
    if s[i]==' ':
        s[i]=' '
    else:
        #subtract  shift number from character index
        nl=a.index(s[i]) - sn
        s[i]=a[nl]
    #convert the list back to a string
p1=''.join(map(str, s))
logging.info('The decrypted message for {} is {}'.format(s,p1))
