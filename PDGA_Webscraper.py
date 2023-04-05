import string
from bs4 import BeautifulSoup
import requests
from csv import writer

url = input('Enter PDGA event url here: ')

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)

    for table in soup.find_all('table', class_='results'):
        header = [th.text.strip() for th in table.find('thead').find_all('th')]
        thewriter.writerow(header)

        for row in table.find('tbody').find_all('tr'):
            data = [td.text.strip() for td in row.find_all('td')]
            thewriter.writerow(data)
