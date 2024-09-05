import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from io import BytesIO
import customtkinter as ctk

def scrape_data():
    url = "https://example.com"  # Replace with your target URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')  # Adjust this according to the website structure

    data = []
    for article in articles:
        header = article.find('h2').get_text()  # Adjust as necessary
        img_url = article.find('img')['src']  # Adjust as necessary
        
        # Fetch image
        img_response = requests.get(img_url)
        img = Image.open(BytesIO(img_response.content))
        img = img.resize((150, 100), Image.Resampling.LANCZOS)  # Resizing the image
        
        data.append((header, img))

    return data

def display_data(data):
    app = ctk.CTk()
    app.title("Web Scraper Results")

    for i, (header, img) in enumerate(data):
        label = ctk.CTkLabel(app, text=header)
        label.grid(row=i, column=0, padx=10, pady=10)
        
        # Convert PIL image to a format compatible with Tkinter
        tk_img = ImageTk.PhotoImage(img)
        img_label = ctk.CTkLabel(app, image=tk_img)
        img_label.image = tk_img  # Keep a reference to avoid garbage collection
        img_label.grid(row=i, column=1, padx=10, pady=10)

    app.mainloop()

if __name__ == "__main__":
    data = scrape_data()
    display_data(data)
