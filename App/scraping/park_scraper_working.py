from bs4 import BeautifulSoup
import requests as req
import csv
import time
import pandas as pd
import os.path

#make a folder named 'data'
if not os.path.exists('data'):
        os.mkdir('data')

#remove previous data if it exists
if os.path.exists('data/national_parks.csv'):
    os.remove('data/national_parks.csv')
    
database=[]
list=['OR','WA','CA']
for state in list: #Remember to update the number of pages 
    url = 'https://www.nps.gov/state/'+state+'/index.htm'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = req.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30)) 
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find_all('li', class_='clearfix'):
        if i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left') == None:
            break
        park=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('h3').text.strip()
        print('Park:',park)
        location=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('h4').text.strip()
        print('Location:', location)
        description=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('p').text.strip()
        print('Description:', description)
        
        database.append((park,location,description))
    
df = pd.DataFrame(database, columns=['park','location','description'])
df.to_csv('data/national_parks.csv', index=False, encoding='utf-8')