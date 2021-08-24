#creating employees using logging
import logging
#setting the logging level to info and logging into a file and changing format of log.
logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
#class of employee
class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        #logging the info of employee
        logging.info('Created Employee:{}-{}'.format(self.fullname,self.email))
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp_1=Employee('sindhu','konda')
emp_2=Employee('vineetha','Sammeta')
emp_3=Employee('vyshnavi','lakkimsetty')