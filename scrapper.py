import requests
from bs4 import BeautifulSoup
import threading
import time

url = "https://nkiri.com/category/international/"
total_pages = 84
threads = []

# Scraper function with better error handling and logging
def scrape_url(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.RequestException as err:
        print(f"Error fetching {url}: {err}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the structure of the webpage is correct
    articles = soup.find_all('article')
    if not articles:
        print(f"No articles found on {url}")
        return
    
    # Adjust the title extraction according to the site's structure
    for article in articles:
        title_tag = article.find('h2')  # Adjust if necessary
        if title_tag:
            title = title_tag.text.strip()
            print(f"Title: {title}")
        else:
            print("Title not found in article")

# Create and manage threads with a smaller batch size
def start_scraping():
    session = requests.Session()  # Create a session object
    for page in range(1, total_pages + 1):
        page_url = f"{url}page/{page}"  # Adjust pagination URL format if needed
        thread = threading.Thread(target=scrape_url, args=(page_url,))
        threads.append(thread)
        thread.start()

        time.sleep(1)  # Add a delay between requests to avoid overloading the server

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_scraping()
