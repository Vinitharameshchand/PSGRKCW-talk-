import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.psgrkcw.ac.in"
response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

# --- Default values (fallback safe values) ---
college_name = "PSGR Krishnammal College for Women, Coimbatore"
location = "Coimbatore, Tamil Nadu, India"
contact = "You can contact the college office at 080-49251252 or email at hr@psgrkcw.ac.in."
accreditation = "The college is affiliated with Bharathiar University and accredited by NAAC."

# --- Try scraping dynamic content safely ---
try:
    title = soup.title.text.strip()
    if title:
        college_name = "PSGR Krishnammal College for Women, Coimbatore"
except:
    pass

# --- FINAL FAQ DATA (STRUCTURED & CLEAN) ---
faqs = [
    {
        "keywords": ["full name of the college", "college full name", "name of the college"],
        "reply": f"The full name of the college is {college_name}."
    },
    {
        "keywords": ["location", "address", "where is the college", "college located"],
        "reply": f"The college is located in {location}."
    },
    {
        "keywords": ["contact", "phone", "email", "office contact"],
        "reply": contact
    },
    {
        "keywords": ["accreditation", "affiliation", "approved", "recognized"],
        "reply": accreditation
    },
    {
        "keywords": ["admission", "apply", "application", "join", "eligibility", "admission start", "admission date", "criteria"],
        "reply": "Admissions are based on merit. Students can apply online through the college website. Eligibility and admission dates are available in the Admissions section."
    },
    {
        "keywords": ["fee", "fees", "fee structure", "payment", "bcom fee", "hostel fee", "transport fee"],
        "reply": "The fee structure varies depending on the course. Please visit the Fees section or contact the college office."
    },
    {
        "keywords": ["course", "courses", "program", "programme", "ug", "undergraduate", "pg", "postgraduate"],
        "reply": "The college offers UG and PG programs in Arts, Science, Commerce, and Computer Science."
    },
    {
        "keywords": ["scholarship", "scholarships", "merit scholarship", "government scholarship", "eligibility for scholarship"],
        "reply": "Government and merit-based scholarships are available for eligible students. Check the Scholarships section for details."
    },
    {
        "keywords": ["placement", "placements", "job", "internship", "company", "package", "career"],
        "reply": "The college provides placement assistance with training and campus recruitment opportunities."
    },
    {
        "keywords": ["hostel", "hostel facility", "girls hostel", "boys hostel", "accommodation"],
        "reply": "Hostel facilities are available for students with food, security, and a study-friendly environment."
    },
    {
        "keywords": ["transport", "bus", "bus routes", "bus timing", "bus facility"],
        "reply": "The college provides bus transport facility. Routes, timings, and transport fee details are available in the Transport section."
    },
    {
        "keywords": ["exam", "exams", "timetable", "hall ticket", "results", "revaluation", "attendance", "academic calendar"],
        "reply": "Exam schedules, hall tickets, results, and academic calendar are available in the Examination & Academics section."
    },
    {
        "keywords": ["library", "digital library", "wifi", "laboratory", "lab", "sports", "gym", "medical", "cafeteria"],
        "reply": "The college provides excellent campus facilities including library, laboratories, sports, gym, medical aid, and cafeteria."
    },
    {
        "keywords": ["grievance", "counseling", "anti-ragging", "clubs", "nss", "ncc", "women safety"],
        "reply": "Student support services include grievance redressal, counseling, anti-ragging committee, student clubs, NSS/NCC, and women safety measures."
    },
    {
        "keywords": ["bonafide certificate", "transfer certificate", "conduct certificate", "course completion certificate"],
        "reply": "You can apply for bonafide, transfer, conduct, and course completion certificates via the college office or website."
    },
    {
        "keywords": ["cultural events", "seminars", "workshops", "annual day", "competitions", "industrial visits", "events"],
        "reply": "The college conducts various events including cultural events, seminars, workshops, annual day, competitions, and industrial visits."
    },
    {
        "keywords": ["hi", "hello", "hey"],
        "reply": "Hello! 👋 How can I help you today?"
    },
    {
        "keywords": ["thank you", "thanks"],
        "reply": "You're welcome! 😊 Happy to help."
    },
    {
        "keywords": ["bye", "exit"],
        "reply": "Thank you for visiting. Have a great day! 👋"
    }
]

# --- Save to JSON ---
with open("../data/faqs1.json", "w", encoding="utf-8") as f:
    json.dump(faqs, f, indent=4, ensure_ascii=False)

print("✅ faqs.json created successfully")
