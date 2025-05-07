import os
print("Saving to:", os.getcwd())
# Step 1: Import Libraries
import requests
from bs4 import BeautifulSoup
import csv

# Step 2: Define the URL
url = "http://books.toscrape.com/"

# Step 3: Send HTTP Request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find All Book Containers
books = soup.find_all('article', class_='product_pod')

# Step 5: Extract Data
book_data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    book_data.append([title, price])

# Step 6: Save to CSV
with open('books_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Book Title', 'Price'])
    writer.writerows(book_data)

print("✅ Scraping Completed. Data saved to books_data.csv.")
