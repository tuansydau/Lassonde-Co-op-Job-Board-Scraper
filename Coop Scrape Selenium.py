from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

import time

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument("— incognito")

un = "216390064"
pw = "***********" #this isnt my password anymore i swear

# replace 'C:/bin/chromedriver.exe' to where chromedriver is installed on your system
browser = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)
browser.get("https://lassondecoop.com/student/login.htm")

time.sleep(10)

# Enter username and password
#usernameBox=browser.find_element_by_xpath('//*[@id=\"j_username\"]')
#usernameBox.click()
#usernameBox.send_keys(un)

#passwordBox=browser.find_element_by_xpath('//*[@id=\"j_password\"]')
#passwordBox.click()
#passwordBox.send_keys(pw + Keys.RETURN)

# go to job board
browser.get('https://lassondecoop.com/myAccount/coop-postings.htm')

time.sleep(5)
# parse html table and save to csv
#with open('page.html', 'w') as f:
#    f.write(browser.page_source)

# edits: change pages? //*[@id="posting9622"]/td[1]/a[1]
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[4]/div/div/div/div/div[4]/div[1]/div[2]/div/div/a[1]').click()

#page 1
content = browser.page_source
with open('webpage.html', 'w') as f:
    f.write(content)
tables = pd.read_html('webpage.html') # Returns list of all tables on page
jobTable=tables[1].drop(['Position Type', 'Unnamed: 5' , 'Unnamed: 6'], axis=1) #refine table
print(jobTable)
jobTable.to_csv(r'C:\Users\tukau\Desktop\datasets\CoopScrape\jobs.csv', index='False')
browser.find_element_by_xpath('//*[@id="postingsTablePlaceholder"]/div/div/div/ul/li[3]/a').click()

# page 2
content = browser.page_source
with open('webpage.html', 'w') as f:
    f.write(content)
tables = pd.read_html('webpage.html', headers='False') # Returns list of all tables on page
jobTable=tables[1].drop(['Position Type', 'Unnamed: 5' , 'Unnamed: 6'], axis=1) #refine table
print(jobTable)
jobTable.to_csv(r'C:\Users\tukau\Desktop\datasets\CoopScrape\jobs.csv', mode='a', index='False')
browser.find_element_by_xpath('//*[@id="postingsTablePlaceholder"]/div/div/div/ul/li[4]/a').click()

# page 3
content = browser.page_source
with open('webpage.html', 'w') as f:
    f.write(content)
tables = pd.read_html('webpage.html', headers='False') # Returns list of all tables on page
jobTable=tables[1].drop(['Position Type', 'Unnamed: 5' , 'Unnamed: 6'], axis=1) #refine table
print(jobTable)
jobTable.to_csv(r'C:\Users\tukau\Desktop\datasets\CoopScrape\jobs.csv', mode='a', index='False')


# page 2 - //*[@id="postingsTablePlaceholder"]/div/div/div/ul/li[3]/a
# page 3 - //*[@id="postingsTablePlaceholder"]/div/div/div/ul/li[4]/a
