# Import BeautifulSoup4 & requests
from bs4 import BeautifulSoup
import requests

# Base URL for book scraping
url = 'https://books.toscrape.com/'
#html = requests.get(url).text
response = requests.get(url)
response.encoding = "utf-8" # Fix encoding issues in CLI
html = response.text # Finally convert encoded response to text
soup = BeautifulSoup(html, 'html.parser')

# Begin for loop to scrape all book contents via {URL}
for books in soup.select(".product_pod"):
    title = books.select_one("h3").get_text() # Get each book title
    price = books.select_one(".price_color").get_text()
    rating = books.select_one(".star-rating")
    stars = rating["class"][1]
    # Finally, print [title + price] & star rating under...
    print(title + " " + price)
    print(stars, "Star Rating...")
    print()
