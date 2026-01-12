import requests
from bs4 import BeautifulSoup
import urllib.parse

def search(username):
    query = f'site:facebook.com "{username}"'
    encoded = urllib.parse.quote(query)
    url = f"https://duckduckgo.com/html/?q={encoded}"

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        if "facebook.com" in a["href"]:
            links.add(a["href"])

    return links


if __name__ == "__main__":
    print("Simple Google Dork OSINT Tool")
    username = input("Enter Username: ")

    results = search(username)

    print("\nResults:\n")
    for link in results:
        print(link)
