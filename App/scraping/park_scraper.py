import requests 
from bs4 import BeautifulSoup

#import time
#import random as rand 

import pandas as pd

database=[]
list=['OR','WA','CA']
for state in list: #Remember to update the number of pages 
    url = 'https://www.nps.gov/state/'+state+'/index.htm'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30)) 
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find_all('li', class_='clearfix'):
        if i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left') == None:
            break
        text=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').text.strip()
        print(text)
            
df = pd.DataFrame(database, columns=['text'])
df.to_csv('user_reviews.csv', index=False, encoding='utf-8')