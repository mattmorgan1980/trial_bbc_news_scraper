import scraperwiki
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("h3", class_="gs-c-promo-heading__title")

for article in articles:
    title = article.text.strip()
    scraperwiki.sqlite.save(unique_keys=["title"], data={"title": title})
