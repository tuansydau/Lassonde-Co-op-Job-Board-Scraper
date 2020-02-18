# Lassonde-Co-op-Job-Board-Scraper
A Python script to scrape information from the Lassonde coop job board using Selenium webdriver and Pandas.

Dependencies:
- Python 3.X
- Selenium webdriver
- Chromedriver
- Pandas

Before use:
- Replace executable path on line 15 with the path of your chromedriver.exe file
- Replace all "C:\Users\tukau\Desktop\datasets\CoopScrape\jobs.csv" paths with the location that you want to save your .csv file ()

How to use:
1. Replace the un variable with your Lassonde co-op log-in, and the pw variable with your password.
2. Run Coop Scrape Selenium.py
3. Scroll down when browser first loads to login screen such that username and password box are in view.
4. When the browser loads the "Co-op Postings" page, scroll down so that the "All Job Postings" button is in view.
5. Wait until all job pages have been clicked.
6. Complete!

Jobs will be saved in a .csv file in the same directory as the Coop Scrape Selenium.py, unless changed.
