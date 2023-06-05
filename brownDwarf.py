
from bs4 import BeautifulSoup as bs
import requests as rec
import pandas as pd


url= 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = rec.get(url)

soup = bs(page.text, 'html.parser')

startable = soup.find_all('table', {"class":"wikitable sortable"})
totalTable = len(startable)

temp = []
tabler = startable[1].find_all('tr')

for tr in tabler:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)

starNames = []
distance = []
mass = []
radius = []

for i in range(1,len(temp)):
    starNames.append(temp[i][0])
    distance.append(temp[i][5])
    mass.append(temp[i][8])
    radius.append(temp[i][9])
    

headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(starNames,distance,mass,radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")