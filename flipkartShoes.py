#import requests
import requests
#import beautiful soup
import bs4
#import logging
import logging
import pandas as pd
logging.basicConfig(filename='flipkartShoes.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(lineno)d~%(funcName)s~%(levelname)s - %(message)s')
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
#A product list to save names of shoes
products=[]
assured=[]
prices=[]
offer_percentage=[]
#running through the tags of shoes
for i in soup.find_all('div', attrs={'class': '_2B099V'}):
    name = i.find('div', attrs={'class': '_2WkVRV'})
    # logging the names of shoes
    logging.info(name.text)
    #adding shoe names to product list
    products.append(name.text)
    # adding assured products or not to list
    try:
        ass = i.find('div', attrs={'class': '_1a8UBa'})
        assured.append('Flipkart Assured')
    except:
        assured.append('Not Flipkart Assured')
    pri= i.find('div', attrs={'class': '_30jeq3'})
    prices.append(pri.text)
    try:
        off= i.find('div', attrs={'class': '_3Ay6Sb'})
        offer_percentage.append(off.text)
    except:
        offer_percentage.append(0)


#a data frame for product list
df=pd.DataFrame({'Product Name':products,'Flipkart Asuurance':assured,'Price of the product':prices,'Offer percentage':offer_percentage})
df.to_csv('flipkartShoes.csv', index=False, encoding='utf-8')
