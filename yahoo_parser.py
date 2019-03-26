from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.read_csv('companylist.csv')
company_list = df['Symbol']

def income_parse(company_list):
    URL = 'https://www.marketwatch.com/investing/stock/fslr/financials/income/quarter'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    financials = soup.find('table', {'class':'crDataTable'}).tbody
    rows = financials.find_all('tr')
#    columns = for v in rows[0].find_all('th')
    print(financials)
    
income_parse(company_list)
