
import requests  
r = requests.get('https://stockx.com/sneakers')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')  
results = soup.find_all('div', attrs={'class':'clickZone'})

records = []  
for result in results:  
    name = result.find('div', attrs={'class': 'name'}).find('div').text
    price = result.find('div', attrs={'class': 'price'}).find('div').contents[1].text
    # url = result.find('a')['href']
    records.append((name, price))

import pandas as pd  
df = pd.DataFrame(records, columns=['name', 'price'])  
# df['date'] = pd.to_datetime(df['date'])  
df.to_csv('eies.csv', index=False, encoding='utf-8') 



