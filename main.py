import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

headers = {'user-agent': USER_AGENT}

query = input('Ask Jeeves: ')
query = query.replace(' ', '+')
url = f'https://google.com/search?q={query}'

response = requests.get(url, headers=headers)

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')

answer = soup.find('span', {'class': 'hgKElc'})
