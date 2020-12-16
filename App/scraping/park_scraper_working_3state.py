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
database1=[]
database2=[]
#list=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA',
      #'HI','ID','IL','IN','IA','KS','KY','LA','ME','MD',
      #'MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
      #'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC',
      #'SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

list=['WA','CA','OR']

for state in list: #Remember to update the number of pages
    print("scraping page " + str(state) + "...")
    url = 'https://www.nps.gov/state/'+state+'/index.htm'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = req.get(url, headers = user_agent)
    time.sleep(5) 
    soup = BeautifulSoup(response.text, 'html.parser')
    #image_wrap_data = soup('img', class_='col-md-12 col-sm-12 col-xs-6 noPadding stateThumbnail')
    for i in soup.find_all('li', class_='clearfix'):
        if i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left') == None:
            break
        park=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('h3').text.strip()
        #print('Park:',park)
        location=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('h4').text.strip()
        #print('Location:', location)
        description=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('p').text.strip()
        if i.find('div', class_='col-md-12 col-sm-12 col-xs-6 noPadding stateThumbnail').find('img') == None:
            break
        image = i.find('div', class_='col-md-12 col-sm-12 col-xs-6 noPadding stateThumbnail').find('img')['src']
        #print('Description:', description)
        if state == 'WA':
            database.append((park,state,location,description,image))
        if state == 'OR':
            database1.append((park,state,location,description,image))
        if state == 'CA':
            database2.append((park,state,location,description,image))
        
print("finished scraping, adding to csv...")        
df = pd.DataFrame(database, columns=['park','state','location','description','image'])
df1 = pd.DataFrame(database1, columns=['park','state','location','description','image'])
df2 = pd.DataFrame(database2, columns=['park','state','location','description','image'])
df.to_csv('data/national_parks_WA.csv', index=False, encoding='utf-8')
df.to_csv('data/national_parks_OR.csv', index=False, encoding='utf-8')
df.to_csv('data/national_parks_CA.csv', index=False, encoding='utf-8')
print("done!")