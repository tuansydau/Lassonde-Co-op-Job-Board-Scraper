from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import selenium

option = webdriver.ChromeOptions()
option.add_argument("— incognito")

un = "216390064"
pw = "peepeepoopoo"

browser = webdriver.Chrome(executable_path=r"C:/bin/chromedriver.exe", options=option)

web_url = "https://lassondecoop.com/student/login.htm"

browser.get(web_url)

usernameBox=browser.find_element_by_xpath("//*[@id=\"j_username\"]")
usernameBox.click()
usernameBox.send_keys(un)

passwordBox=browser.find_element_by_xpath("//*[@id=\"j_password\"]")
passwordBox.click()
passwordBox.send_keys(pw + Keys.RETURN)

browser.implicitly_wait(4)

browser.navigate().to('https://lassondecoop.com/myAccount/coop-postings.htm')


# browser.find_element_by_xpath("//*[@id=\"loginForm\"]/div[3]/input").click()

# wait

# browser.implicitly_wait(5)

# browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/ul/li[10]/a').click()


# usernameBox = browser.find_element_by_id('box')
# usernameBox.send_keys('python')
