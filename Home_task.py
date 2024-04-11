import requests
from bs4 import BeautifulSoup
import json

url = "https://spb.hh.ru/search/vacancy?text=Python+developer&from=suggest_post&salary=&ored_clusters=true&area=2&area=1&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

jobs = []

for job_elem in soup.find_all(class_="job"):
    title = job_elem.find("a", class_="vt").text.strip()
    link = job_elem.find("a")["href"]
    salary = job_elem.find("span", class_="salary").text.strip()
    company = job_elem.find("span", class_="company_name").text.strip()
    city = job_elem.find("span", class_="location").text.strip()

    description = job_elem.find("div", class_="text").text.strip().lower()
    if "django" in description and "flask" in description:
        job_info = {
            "title": title,
            "link": link,
            "salary": salary,
            "company": company,
            "city": city
        }
        jobs.append(job_info)

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=4)
