import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.psgrkcw.ac.in/ug-programmes/"
response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for p in soup.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) > 50:
        data.append({
            "question": "UG Courses information",
            "reply": text,
            "keywords": ["ug", "ug courses", "ug course"]
        })

with open("../data/ugcourses.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("UG Courses data scraped")
