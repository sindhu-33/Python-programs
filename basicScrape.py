#import requests
import requests
#import beautiful soup
import bs4
#import logging
import logging
logging.basicConfig(filename='basicScrape.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
#setting up a request with variable res
res=requests.get('https://www.flipkart.com/womens-footwear/pr?sid=osp,iko&otracker=nmenu_sub_Women_0_Footwear')
#logging the type of request 'res' variable
logging.info(type(res))
soup=bs4.BeautifulSoup(res.text,'lxml')
#logging the type of soup variable
logging.info(type(soup))
t1=soup.select('title')
#logging the complete list extracted from webpage
logging.info(t1)
#logging only title text from webpage
logging.info(t1[0].getText())