from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.read_csv('companylist.csv')
company_list = df['Symbol']

def income_parse(company_list):
    URL = 'https://www.marketwatch.com/investing/stock/fslr/financials/income/quarter'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    financials = soup.find_all('table', class_='crDataTable')

    for lines in financials:
        rows = lines.find_all('tr')
        
    print(lines)



'''
            tds = element.find_all(class_="rowTitle")
            td = element.find_all(class_="valueCell")
    print(financials)
#            values = [td in tds]
#
#            df = df.append(pd.Series(values)
            


    
'''    
    
income_parse(company_list)
