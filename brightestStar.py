
from bs4 import BeautifulSoup as bs
import requests as rec
import pandas as pd


url= 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = rec.get(url)

soup = bs(page.text, 'html.parser')

bstartable = soup.find('table')
btotalTable = len(bstartable)

temp = []
tabler = bstartable.find_all('tr')

for tr in tabler:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)

starNames = []
distance = []
mass = []
radius = []
luminosity = []

for i in range(1,len(temp)):
    starNames.append(temp[i][1])
    distance.append(temp[i][3])
    mass.append(temp[i][5])
    radius.append(temp[i][6])
    luminosity.append(temp[1][7])
    

headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(starNames,distance,mass,radius,luminosity,)),columns=['Star_name','Distance','Mass','Radius', 'luminosity'])
print(df2)

df2.to_csv('brightest_stars.csv', index=True, index_label="id")