"""make the import statement"""

import requests
from bs4 import BeautifulSoup

url = "https://www.tvcnews.tv/"
response = requests.get(url)
print("print found")

if response.status_code == 200:
    print("print found")
    print(f"Error:{response.status_code}")
   #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    for data in soup.find_all('div',{'class':'jeg_posts_wrap'}):
        title = data.find('h3').text.strip()
        print(title)


   