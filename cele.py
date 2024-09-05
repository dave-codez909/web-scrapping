from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import threading

url = "https://nkiri.com/category/international/"
total_pages = 84

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Path to the chromedriver executable
chrome_driver_path = "path/to/chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_url(page_url):
    driver.get(page_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for article in soup.find_all('article'):
        title = article.find('h2', class_='entry-title').text.strip()
        print(title)

threads = []

for page in range(1, total_pages + 1):
    page_url = f"{url}?page={page}"
    thread = threading.Thread(target=scrape_url, args=(page_url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

driver.quit()
