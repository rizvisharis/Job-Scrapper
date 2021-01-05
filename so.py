import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = (f"https://stackoverflow.com/jobs?q=python&pg=2")

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div", {"class", "s-pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_page = get_last_page()
    return []