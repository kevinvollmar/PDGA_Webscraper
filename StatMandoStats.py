import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a request to the URL
url = "https://statmando.com/rankings/dgpt/mpo"
res = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(res.text, "html.parser")

# Find the table containing the standings
table = soup.find("table")

# Create a list to hold the rows of the table
rows = []

# Iterate over the rows of the table and extract the data
for row in table.find_all("tr"):
    # Get the cells of the row
    cells = row.find_all("td")
    # Extract the text from each cell and add it to the row list
    row_list = []
    for cell in cells:
        row_list.append(cell.get_text().strip())
    # Add the row to the rows list
    if row_list:
        rows.append(row_list)

# Convert the rows list to a pandas DataFrame
df = pd.DataFrame(rows, columns=rows[0])

# Print basic statistics about the table
print(df.iloc[1:]['Points'].describe())

