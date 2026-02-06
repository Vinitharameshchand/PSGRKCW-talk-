import json

with open("data/faqs.json") as f:
    faqs = json.load(f)

with open("data/courses.json") as f:
    courses = json.load(f)

def get_bot_response(user_input):
    text = user_input.lower()

    if "course" in text:
        return "Available courses: " + ", ".join(courses.keys())

    for faq in faqs:
        if faq["question"].lower() in text:
            return faq["answer"]

    return "Please contact the college office for detailed information."
