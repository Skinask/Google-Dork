import requests
from bs4 import BeautifulSoup
import urllib.parse

username = input("Enter Username: ")

query = f'site:facebook.com "{username}"'
encoded_query = urllib.parse.quote(query)

url = f"https://duckduckgo.com/html/?q={encoded_query}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

links = set()

for a in soup.find_all("a", href=True):
    href = a["href"]
    if "facebook.com" in href:
        links.add(href)

print("\nPossible Facebook URLs:\n")
for link in links:
    print(link)