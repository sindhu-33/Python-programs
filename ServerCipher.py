import socket
import logging
import string
a=string.ascii_lowercase+string.ascii_lowercase
logging.basicConfig(filename='ServerCipher.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#creating a socket
s=socket.socket()
#logging the info into file.
logging.info('Socket Created')
#binding with a port
s.bind(('localhost',9223))
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
    # taking the shift number from user
    sn=int(input('enter your shift number from 1 to 25:\n'))
    logging.info('The shift number taken from user is {}'.format(sn))
    #Open the file as w to write string
    file=open('ServerEncrypt.key','w')
    #write the shift number into file
    file.write(str(sn))
    #close the file
    file.close()
    s1=input('enter the string to encrypt\n')
    #logging the enncoded msg
    logging.info('The message passing to the client is {}'.format(s))
    #encypting the message
    s1=list(s1)
    for i in range(len(s1)):
        #get the position of each character within the sentence
        if s1[i]==' ':
            s1[i]=' '
        else:
            #add the shift number to character
            nl=a.index(s1[i])+sn
            s1[i]=a[nl]
    #convert the list back to a string
    p1=''.join(map(str,s1))
    #logging the encrypted message
    logging.info('The encrypted message for {} is {}'.format(s1,p1))
    #sending the encrypted message to the client
    c.send(p1.encode())
    #close the connection
    c.close()

