from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#C:\Users\livcr\OneDrive\Pictures\chromedriver_win32
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/livcr/OneDrive/Pictures/chromedriver_win32/chromedriver.exe")
browser.get(url)
time.sleep(10)


scrapedData = []

def scrape():
  soup=BeautifulSoup(browser.page_source, "html.parser")
  bst = soup.find("table", attrs={"class", "wikitable"})

  tbody = bst.find("tbody")

  trows = tbody.find_all("tr")

  for row in trows:
    tcol = row.find_all("td")
    print(tcol)
    tempList = []
    for coldata in tcol:
      data = coldata.text.strip()
      tempList.append(data)
      print(tempList)
    scrapedData.append(tempList)

#calling function
scrape()

starData = []

for i in range(0,len(scrapedData)):

  name = scrapedData[i][1]
  distance = scrapedData[i][3]
  mass = scrapedData[i][5]
  radius = scrapedData[i][6]
  lum = scrapedData[i][7]

  requiredData = [name, distance, mass, radius, lum]
  starData.append(requiredData)
print(starData)

headers = ['name', 'distance', 'mass', 'radius', 'lum']

definestar1 = pd.DataFrame(starData, columns = headers)

definestar1.to_csv('scraped.csv', index = True, index_label = 'id')