import requests
from bs4 import BeautifulSoup

webhook_url = 'https://discord.com/api/webhooks/876773577427402752/Rw-CsX_Ix7NxIlQAo6NyTCmK06IDgush6ocwvt768iNrnaEPeW-z7NC6pvbjam6DXlMc'

for i in range(8730, 10100):

    url = f'https://www.bmeme.hu/post/{i}'
    html_doc = requests.get(url).content
    soup = BeautifulSoup(html_doc, 'html.parser')

    meme = soup.find('img')
    meme_tag = soup.find('h4').string # mém tagje

    if meme_tag == 'BME': # milyen tag érdekel
        number_of_likes = soup.find('div', class_='like_counter').find('span').string
        if int(number_of_likes) > 0: # a szar mémeket mellőzi
            image_url = meme['src']  # a hírhez tartozó kép
            print(f'https://www.bmeme.hu{image_url}')
