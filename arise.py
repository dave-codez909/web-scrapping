import requests
from bs4 import BeautifulSoup
import threading

# Define the function that will be executed by each thread
def fetch_content(numb):
    url = f"https://www.arise.tv/category/sports/page/{numb}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for data in soup.find_all('article'):
        title = data.find('h3').text.strip()
        img_tag = data.find('img')
        img_url = img_tag['src'] if img_tag else 'No image found'
        
        print(f"Title: {title}")
        print(f"Image URL: {img_url}")
        print("-" * 50)

# Number of pages to scrape
total_pages = 117

# Create a thread for each page
threads = []
for numb in range(1, total_pages + 1):  # Assuming the pages start from 1
    thread = threading.Thread(target=fetch_content, args=(numb,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Scraping completed.")
