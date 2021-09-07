from cryptography.fernet import Fernet
import logging
logging.basicConfig(filename='Sym_encryption.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#generating key to encrypt the string
key=Fernet.generate_key()
#logging the key
logging.info(key)
#encoding the string
msg="My name is sindhu".encode()
#logging the enncoded msg
logging.info(msg)
f=Fernet(key)
#encypting the message
enc=f.encrypt(msg)
#logging the encrypted message
logging.info(enc)
f1=Fernet(key)
#decrypting the message
dec=f1.decrypt(enc)
#logging the decrypted message
logging.info(dec)
