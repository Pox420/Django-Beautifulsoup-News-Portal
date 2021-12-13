from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = 'https://kathmandupost.com/'
r = requests.get(URL)
soup = bs(r.text, 'html.parser')

main =soup.find("div", {"id": "mainContent"}).find('main').find('div', {'class': 'order'}).find_all('div')[0:2]
homepage_url = []

for i in main:
    links = i.find_all('article')
    for j in links:
        link = 'https://kathmandupost.com' +j.find('h3').find('a').get('href')
        homepage_url.append(link)


page_details = []
for home in homepage_url:
    r = requests.get(home)
    soup = bs(r.text, 'html.parser')
    title = soup.find('title').text
    try:
        image_link = soup.find('main').find('div', {'class': 'col-sm-12'}).find('img').get('src')
    except:
        image_link = soup.find('main').find('div', {'class': 'col-sm-8'}).find('img').get('src')
    try:
        sub_title = soup.find('main').find('div', {'class': 'col-sm-12'}).find('span').text
    except:
        sub_title = soup.find('main').find('div', {'class': 'col-sm-8'}).find('span').text
    try:
        main_content = soup.find('main').find('div', {'class': 'col-sm-12'}).find('section').text
    except:
        main_content = soup.find('main').find('div', {'class': 'col-sm-8'}).find('section').text
    # print(title, image_link, sub_title, main_content)
    detail = {
        'title': title,
        'image_link': image_link,
        'sub_title': sub_title,
        'main_content': main_content
    }
    page_details.append(detail)

# print(type('page_details'))


# df = pd.DataFrame(page_details)
# df.to_csv('kathmandu_post.csv')