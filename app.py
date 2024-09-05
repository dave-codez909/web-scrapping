import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the AIT homepage
url = "https://ait.live/"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all relevant article blocks
for data in soup.find_all('div', {'class': 'jeg_postblock_content'}):
    # Extract the title of each article
    title = data.find('h3', {'class': 'jeg_post_title'}).text.strip()
    print(title)
