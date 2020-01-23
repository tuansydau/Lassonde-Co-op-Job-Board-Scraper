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

browser.implicitly_wait(4)
# Enter username and password
usernameBox=browser.find_element_by_xpath('//*[@id=\"j_username\"]')
usernameBox.click()
usernameBox.send_keys(un)

passwordBox=browser.find_element_by_xpath('//*[@id=\"j_password\"]')
passwordBox.click()
passwordBox.send_keys(pw + Keys.RETURN)

# go to job board
browser.get('https://lassondecoop.com/myAccount/coop-postings.htm')

time.sleep(5)
# parse html table and save to csv
#with open('page.html', 'w') as f:
#    f.write(browser.page_source)

# edits: change pages? //*[@id="posting9622"]/td[1]/a[1]
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[4]/div/div/div/div/div[4]/div[1]/div[2]/div/div/a[1]').click()

content = browser.page_source

with open('webpage.html', 'w') as f:
    f.write(content)

tables = pd.read_html('webpage.html') # Returns list of all tables on page
print(tables[0])

# page 2 - //*[@id="postingsTablePlaceholder"]/div/div/div/ul/li[3]/a
# page 3 - //*[@id="postingsTablePlaceholder"]/div/div/div/ul/li[4]/a


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, "html.parser")
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')
# row_list = list()
