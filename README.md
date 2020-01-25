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
2. Run script.
3. Scroll down when browser first loads to login screen, scroll down so that username and password box are in view.
4. When the browser loads the "Co-op Postings" page, scroll down so that the "All Job Postings" button is in view.
5. Jobs will be saved in a .csv

Known bugs:
- Will not work if the number of pages of job postings is not equal to 3
- ID of final jobs.csv file is not accurate
- Not fully automated (scrolling input is required)
