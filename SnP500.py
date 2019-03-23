import bs4 as bs
import requests

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0,1,3,4,5].text
        tickers.append(ticker)
        
    with open("sp500tickers.csv","wb") as f:
        f.write(tickers)
        
    return tickers

save_sp500_tickers()