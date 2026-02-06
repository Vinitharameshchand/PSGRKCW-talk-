import json

with open("data/fees.json") as f:
    fees = json.load(f)

def calculate_fee(course, category):
    return fees.get(course, {}).get(category, "Fee not available")
