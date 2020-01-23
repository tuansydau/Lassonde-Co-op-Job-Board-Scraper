import pandas as pd

import numpy as np

#desired_width=320
#pd.set_option('display.width', desired_width)
#np.set_printoption(linewidth=desired_width)

#pd.set_option('display.max_columns', 10)
tables = pd.read_html('webpage.html') # Returns list of all tables on page

jobTable=tables[1].drop(['Position Type', 'Unnamed: 5' , 'Unnamed: 6'], axis=1)
print(jobTable)

jobTable.to_csv(r'C:\Users\tukau\Desktop\datasets\CoopScrape\jobs.csv', index='False')
