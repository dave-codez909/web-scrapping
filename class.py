import requests
from bs4 import BeautifulSoup

url = "https://www.tvcnews.tv/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for data in soup.find_all('div', {'class':'jeg_posts_wrap'}):
    url = data.find('a')
    if url:
        link = url.get('href')
        print(link)
    

    image = data.find('img')
    if image:
        img = image.get('src')
        print(img)
    print("\n")