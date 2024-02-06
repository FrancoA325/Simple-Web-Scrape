# packages used:
import pandas as pd 
from bs4 import BeautifulSoup
import requests

# connecting to the url and veriying connection
url = 'https://webpages.charlotte.edu/mscipion/'
req = requests.get(url)
print(req)

# using bs4, html.parser to find all of the tables on the page
soup = BeautifulSoup(req.text, "html.parser")
table = soup.find("table")

# looking at the table and pulling the headers and using them to make column names for the dataframe
tableHeaders = table.find_all('th')
titles = []

for i in tableHeaders:
    title = i.text
    titles.append(title)
    
# build the final table dataframe with the column headers as the scraped headers
fullTable = pd.DataFrame(columns = titles)

# scrape the row names from the site
tableRows = table.find_all('tr')

# iterates through rows of the table, then creates the data for each row
for i in tableRows[1:]:
    # data is scraped per table row
    tableData = i.find_all('td')
    # makes row that is the table row text for every line in tableData
    row = [tr.text for tr in tableData]
    # increasing the length of the dataframe as we loop through the table
    l = len(fullTable)
    # .loc[l] is used to iterate through the dataframe as we increase the length and populates the new row with the row data scraped above
    fullTable.loc[l] = row
# grabs the first ten values but the table is only 6 long and prints the dataframe.
fullTable.head(10)
print(fullTable)

