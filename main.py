import requests
from bs4 import BeautifulSoup
import os

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

headers = {'user-agent': USER_AGENT}

while True:
    query = input('Ask Jeeves: ')
    query = query.replace(' ', '+')
    url = f'https://google.com/search?q={query}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')

    answer_one = soup.find('span', {'class': 'hgKElc'})
    try:
        print(answer_one.text)
    except AttributeError:
        answer_two = soup.find('div', class_='Z0LcW')
        try:
            print(answer_two.text)
        except AttributeError:
            answer_three = soup.find_all('li', class_='TrT0Xe')
            if len(answer_three) > 0:
                try:
                    for answer in answer_three[:10]:   
                        print(answer.text.split('.')[0])
                except AttributeError:
                    print('Unable to find an answer. Sorry :(')
            else: 
                answer_four = soup.find_all('a', class_='ct5Ked')
                try:
                    for answer in answer_four[:10]:
                        print(answer['data-entityname'])
                except AttributeError:
                    print('Unable to find an answer. Sorry :(')



                    