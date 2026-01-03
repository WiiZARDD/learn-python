# From BeautifulSoup4, import BeautifulSoup class
from bs4 import BeautifulSoup

# URL for scraping
url = 'https://quotes.toscrape.com/'
# Fetch text from URL --> Store it as (HTML)
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

# Since there is multiple quotes, start a for loop to display each one seperately until they're all shown
# Select ".quote" element for (quotes)
for quotes in soup.select(".quote"):
    # Within quotes elements, select ".text" element one by one and get text
    text = quotes.select_one(".text").get_text()
    # Get text for tag, since there may be multiple, run a for loop to get all tags...
    tags = [t.get_text() for t in quotes.select(".tag")]

    # Finally, print the output
    print(text)
    print("tags: ", tags)
    print()
