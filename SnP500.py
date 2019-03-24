from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class':'wikitable sortable'}).tbody

rows = table.find_all('tr')

columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')

    values = [td.text.replace('\n', '') for td in tds]

    df = df.append(pd.Series(values, index=columns), ignore_index=True)
    df.to_csv('companylist.csv', index=False)
