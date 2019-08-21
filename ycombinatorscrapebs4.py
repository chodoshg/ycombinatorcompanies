from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import pandas as pd 

options = Options()
options.add_argument('--headless')

# alternative non-headless option browser = webdriver.Firefox()

driver = webdriver.Firefox(options=options)

# alternative non-headless option browser.get('https://careers.jobscore.com/careers/lytics')

driver.get('https://www.ycombinator.com/companies/')

data = driver.page_source

soup = BeautifulSoup(data, "html.parser")

#we use the html parser to parse the url content and store it in a variable.textContent = []

#scrape information from website using for loop based on class of different elements

company_list = []
for company in soup.find_all('td', class_='name'):
    company_list.append(company.text)


batch_list = []
for batch in soup.find_all('td', class_='batch'):
    ybatch = str(batch)
    batch_list.append(ybatch[18:-5])


descr_list = []
for descr in soup.find_all("td", class_=False):
    ytext = str(descr)
    descr_list.append(ytext[4:-5])

#Create dictionary from 3 lists (each list a column)

ydict = {'Company':company_list,'Batch':batch_list,'Description':descr_list}

# Create dataframe from dictionary

ydf = pd.DataFrame(ydict)

ydf.to_excel("ycombinatorcompanies.xlsx", sheet_name='Current List',index=False)

driver.quit()
