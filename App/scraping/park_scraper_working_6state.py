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
database3=[]
database4=[]
database5=[]
#list=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA',
      #'HI','ID','IL','IN','IA','KS','KY','LA','ME','MD',
      #'MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
      #'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC',
      #'SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

list=['WA','CA','OR','NY','FL','PA']

for state in list: 
    print("scraping page " + str(state) + "...")
    url = 'https://www.nps.gov/state/'+state+'/index.htm'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = req.get(url, headers = user_agent)
    time.sleep(5) 
    soup = BeautifulSoup(response.text, 'html.parser')
    #image_wrap_data = soup('img', class_='col-md-12 col-sm-12 col-xs-6 noPadding stateThumbnail')
    for i in soup.find_all('li', class_='clearfix'):
        if i.find('img', class_='stateResultImage') == None:
            image = 'None'
        else:
            image = i.find('div', class_='col-md-12 col-sm-12 col-xs-6 noPadding stateThumbnail').find('img')['src']
            image = '<img src=https://www.nps.gov/'+image+'></img>'
        if i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left') == None:
            break
        park=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('h3').text.strip()
        #print('Park:',park)
        location=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('h4').text.strip()
        #print('Location:', location)
        description=i.find('div', class_='col-md-9 col-sm-9 col-xs-12 table-cell list_left').find('p').text.strip()
        
        #print('Description:', description)
        if state == 'WA':
            database.append((park,image,location,description))
        if state == 'CA':
            database1.append((park,image,location,description))
        if state == 'OR':
            database2.append((park,image,location,description))
        if state == 'NY':
            database3.append((park,image,location,description))
        if state == 'FL':
            database4.append((park,image,location,description))
        if state == 'PA':
            database5.append((park,image,location,description))
        
print("finished scraping, adding to csv...")        
df = pd.DataFrame(database, columns=['park','image','location','description'])
df1 = pd.DataFrame(database1, columns=['park','image','location','description'])
df2 = pd.DataFrame(database2, columns=['park','image','location','description'])
df3 = pd.DataFrame(database3, columns=['park','image','location','description'])
df4 = pd.DataFrame(database4, columns=['park','image','location','description'])
df5 = pd.DataFrame(database5, columns=['park','image','location','description'])
df.to_csv('data/national_parks_WA.csv', index=False, encoding='utf-8')
df1.to_csv('data/national_parks_CA.csv', index=False, encoding='utf-8')
df2.to_csv('data/national_parks_OR.csv', index=False, encoding='utf-8')
df3.to_csv('data/national_parks_NY.csv', index=False, encoding='utf-8')
df4.to_csv('data/national_parks_FL.csv', index=False, encoding='utf-8')
df5.to_csv('data/national_parks_PA.csv', index=False, encoding='utf-8')
print("done!")