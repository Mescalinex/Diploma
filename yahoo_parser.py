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
    rows = []
    for lines in financials:
        values = lines.find_all('td')
        rows.append(values)
    
    print(financials)
    
income_parse(company_list)
