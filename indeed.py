import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = (f"https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt="
                            f"all&st=&salary=&radius=25&l=&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch")
def extract_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
      result = requests.get(f"{URL}&start={last_page*LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      results= soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
      for result in results:
        title = result.find("a")["title"]
        company = result.find("span",{"class":"company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
        company = company.strip()
        print(title,company)