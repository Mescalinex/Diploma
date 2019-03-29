from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.read_csv('companylist.csv')
company_list = df['Symbol']

def income_parse():
    # Мы берем URL, который нам нужно скачать
    URL = 'https://www.marketwatch.com/investing/stock/fslr/financials/income/quarter'

    # Отдаем этот URL в requests, он заходит и скачивает нам нужную страницу.
    response = requests.get(URL)

    # Парсим скаченную страницу парсером lxml и складываем html-код в переменную
    soup = BeautifulSoup(response.text, 'lxml')

    # Среди HTML-кода ищем таблицы, у которых указан класс crDataTable
    financials = soup.find_all('table', class_='crDataTable')

    # в Financials у нас лежит некий класс ResultSet
    #print(type(financials))

    # По факту, это список из кусочков того кода, что мы раньше искали. Каждый кусочек - это целая таблица crDataTable
    # Проверим, сколько их там? Столько, сколько и на сайте - 2
    #print(len(financials))
    
    # Мы можем посмотреть, что внутри каждого кусочка - нужная нам таблица. Напечатаем первую таблицу
    #print(financials[0])
    
    # Мы можем найти все нужные нам строчки в этой таблице (нулевой таблице)
    #rows = financials[0].find_all('tr')
    #print(rows)
    
    # А можем поискать только строку, которая нам нужна
    #revenue_row = financials[0].find('tr', class_='partialSum')
    #print(revenue_row)
    
    # А теперь давай найдем для начала, что лежит в этой строчке - Sales/Revenue
    #name_of_financial = revenue_row.find('td', class_='rowTitle').text
    #print(name_of_financial)
    
    # А как посмотреть на значения, которые лежат по датам?
    #revenue_row_values = revenue_row.find_all('td', class_='valueCell')
    #print(revenue_row_values[0].text)
    
    
    # А все значения?
    #for element in revenue_row_values:
    #   print(element.text)

    # А как понять, к каким датам они относятся? Ведь у нас есть заглавная строчка
    #top_row = financials[0].find('tr', class_='topRow')
    #print(top_row)
    #dates = top_row.find_all('th', { 'scope' : 'col' })
    #print(dates[0].text)
    
income_parse()
