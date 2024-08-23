import requests
from bs4 import BeautifulSoup

url = "https://www.arise.tv/category/sports/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for data in soup.find_all('div', {'class': 'article-content'}):
    title = data.find('h3').text.strip()
    print(title)


