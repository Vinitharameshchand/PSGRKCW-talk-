import json
import glob

all_faqs = []

for file in glob.glob("data/faq*.json"):
    with open(file, "r", encoding="utf-8") as f:
        all_faqs.extend(json.load(f))

with open("data/faqs_merged.json", "w", encoding="utf-8") as f:
    json.dump(all_faqs, f, indent=4, ensure_ascii=False)

print("✅ All domain FAQs merged successfully")
