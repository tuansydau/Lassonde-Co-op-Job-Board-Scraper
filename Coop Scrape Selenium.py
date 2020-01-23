from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import selenium
import time

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument("— incognito")
un = "216390064"
pw = "peepeepoopoo" #this isnt my password anymore i swear



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
browser.implicitly_wait(4)
browser.get('https://lassondecoop.com/myAccount/coop-postings.htm')
#jobBoardButton=browser.find_element_by_xpath('//*[@id="dashboard"]/div[4]/div[1]/div[2]/div/div/a[1]')
#jobBoardButton.click()


time.sleep(5)
browser.implicitly_wait(4)
# parse html table and save to csv
#with open('page.html', 'w') as f:
#    f.write(browser.page_source)

# edits: change pages? //*[@id="posting9622"]/td[1]/a[1]
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[4]/div/div/div/div/div[4]/div[1]/div[2]/div/div/a[1]').click();
