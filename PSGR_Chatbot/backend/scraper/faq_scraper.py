import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.psgrkcw.ac.in/faqs/"
response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

faqs = []

for item in soup.find_all("li"):
    q = item.find("strong")
    a = item.find("p")
    if q and a:
        faqs.append({
            "question": q.get_text(strip=True),
            "answer": a.get_text(strip=True),
            "domain": "FAQ"
        })

with open("../data/faqs.json", "w", encoding="utf-8") as f:
    json.dump(faqs, f, indent=2, ensure_ascii=False)

print("FAQ scraping completed.")
