import string
import logging
logging.basicConfig(filename='cipher.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
a=string.ascii_lowercase+string.ascii_lowercase
#take the string input from user
s=list(input('enter your text:\n').lower())
logging.info('The string taken from user is {}'.format(s))
#taking the shift number from user
sn= int(input('enter your shift number from 1 to 25:\n'))
logging.info('The shift number taken from user is {}'.format(sn))
#variable to end the program
ep=False
while not ep:
    # ask the user to select the option
    opt=int(input('enter 1 to ENCRYPT\nenter 2 to DECRYPT\nenter 3 to END program\n'))
    # search through the enter text
    if opt==1:
        #encrypt the string
        for i in range(len(s)):
            # get the position of each character within the sentence
            if s[i]==' ':
                s[i]=' '
            else:
                #add the shift number to character
                nl=a.index(s[i])+sn
                s[i]=a[nl]
        # convert the list back to a string
        p1=''.join(map(str,s))
        logging.info('The encrypted message for {} is {}'.format(s,p1))
    elif opt==2:
        for i in range(len(s)):
            if s[i]==' ':
                s[i]=' '
            else:
                #subtract  shift number from character index
                nl=a.index(s[i])-sn
                s[i]=a[nl]
            # convert the list back to a string
        p1=''.join(map(str, s))
        logging.info('The decrypted message for {} is {}'.format(s,p1))
    elif opt==3:
        ep=True
    else:
        opt2=input('invalid entry, try again Y for YES, N for NO: \n').lower()
        if opt2=='y':
            s=list(input('enter your text: \n').lower())
            logging.info('The string taken from user is {}'.format(s))
            # taking the shift number from user
            sn=int(input('enter your shift number from 1 to 25:\n'))
            logging.info('The shift number taken from user is {}'.format(sn))
        else:
            ep=True