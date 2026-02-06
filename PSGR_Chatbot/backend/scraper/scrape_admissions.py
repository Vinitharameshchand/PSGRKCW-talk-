import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.psgrkcw.ac.in/admissions"
response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for p in soup.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) > 50:
        data.append({
            "question": "Admission information",
            "reply": text,
            "keywords": ["admission", "apply", "eligibility"]
        })

with open("../data/admissions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Admissions data scraped")
