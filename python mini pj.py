import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
page = 1

while True:
    response = requests.get(f"{url}/page/{page}/")
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        break

    found = False

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        # check both love and smile
        if "love" in tags or "smile" in tags:
            print("💖 Quote:", text)
            print("👤 Author:", author)
            print("🏷️ Tags:", tags)
            print("-" * 40)
            found = True

    page += 1

    if not found:
        break