from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("— incognito")

browser = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)
browser.get("https://lassondecoop.com/student/login.htm")

time.sleep(30)

content = browser.page_source

with open('webpage.html', 'w') as f:
    f.write(content)
