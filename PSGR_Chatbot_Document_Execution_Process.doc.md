**PSGRKCW COLLEGE CHATBOT**

**OBJECTIVE**

	The main objective of this project is to design and develop a **locally deployed, AI-based chatbot** for the PSGR Krishnammal College for Women website to provide **quick, accurate, and domain-specific information** to students, parents, and visitors. The chatbot aims to answer user queries related to **admissions, courses, fee structure, placements, events, campus services, and frequently asked questions** using **structured and maintainable data**.

This project focuses on achieving:

* Structured domain-wise information retrieval  
* Clear and accurate responses for user queries  
* Easy future maintenance through JSON-based knowledge storage  
* Local deployment without modifying the existing college website infrastructure  
* Improved accessibility to college information through a conversational interface

**ABSTRACT**

	In the digital era, educational institutions require efficient systems to provide instant information to students and visitors. This project presents the development of a **college information chatbot** for PSGR Krishnammal College for Women using **Python, Flask, and web-scraping techniques**. The chatbot is designed to operate as a **locally hosted web application**, eliminating the need for changes to the existing college website or server infrastructure.

	The system extracts publicly available information from the college website using **BeautifulSoup** and organizes it into **structured, domain-wise JSON files** covering admissions, courses, fee structure, placements, events, campus services, and FAQs. A keyword-based retrieval mechanism is implemented to ensure **accurate and relevant responses** to user queries. The chatbot interacts with users through a simple web interface built using **HTML, CSS, and JavaScript**, while the backend processes requests using a **RESTful Flask API**.

	The proposed solution enhances user experience by providing **instant, clear, and reliable information**, reduces manual inquiry workload, and ensures easy scalability and maintenance. The project demonstrates an effective approach to building an AI-assisted information system for educational institutions using lightweight technologies and local deployment.

**PROBLEM STATEMENT**

	Educational institutions often receive a large number of repetitive queries related to admissions, courses, fees, placements, events, and campus facilities. Currently, users must navigate multiple web pages or rely on manual support to obtain this information, which can be time-consuming and inefficient. Additionally, maintaining and updating such information on a live website requires server access and technical intervention.

	There is a need for a **user-friendly, automated system** that can provide **instant and accurate responses** to frequently asked questions without modifying the existing college website infrastructure. The system should be easy to maintain, scalable, and capable of handling domain-specific queries efficiently.

**SCOPE OF THE PROJECT**

The scope of this project includes:

* Development of a **local, web-based chatbot** for college information retrieval  
* Extraction of publicly available data from the college website using **web scraping techniques**  
* Organization of data into **structured, domain-wise JSON files**  
* Handling queries related to:  
  * Admissions  
  * Courses offered  
  * Fee structure  
  * Placement statistics  
  * Events and activities  
  * Campus services  
  * Frequently asked questions  
* Providing a **separate placement statistics dashboard**  
* Ensuring **local deployment** without integrating into the college website’s cPanel

The project does not include:

* Modification of the official college website  
* Real-time database integration  
* Authentication or payment processing

**SYSTEM ARCHITECTURE** 

**Architecture Overview**

The system follows a **client-server architecture** with a clear separation between frontend and backend components.

**Components**

1. **Frontend (Client Side)**  
   * Developed using HTML, CSS, and JavaScript  
   * Provides a chatbot interface for user interaction  
   * Sends user queries to the backend via HTTP requests  
2. **Backend (Server Side)**  
   * Implemented using Python and Flask  
   * Exposes a RESTful API endpoint (/chat)  
   * Processes user queries and retrieves relevant responses  
3. **Knowledge Base (JSON Files)**  
   * Stores structured domain-wise information  
   * Each entry contains keywords and corresponding replies  
   * Enables easy updates without changing application logic  
4. **Web Scraping Module**  
   * Uses BeautifulSoup and Requests libraries  
   * Extracts publicly available content from the college website  
   * Converts extracted data into structured JSON format

**Working Flow**

1. User enters a query in the chatbot interface  
2. Query is sent to the Flask backend via POST request  
3. Backend searches the JSON knowledge base using keyword matching  
4. Best matching response is identified  
5. Answer is returned and displayed to the user

**PROJECT STRUCTURE** 

psgrkcw-chatbot/  
│  
├── backend/  
│   ├── app.py                    \# Flask chatbot API  
│   ├── requirements.txt          \# Python dependencies  
│   │  
│   ├── data/                     \# Structured domain-wise knowledge  
│   │   ├── admissions.json  
│   │   ├── courses.json  
│   │   ├── fees.json  
│   │   ├── placements.json  
│   │   ├── events.json  
│   │   ├── services.json  
│   │   └── faqs.json  
│   │  
│   └── scraper/                  \# Web scraping scripts  
│       ├── scrape\_admissions.py  
│       ├── scrape\_courses.py  
│       ├── scrape\_fees.py  
│       ├── scrape\_placements.py  
│       ├── scrape\_events.py  
│       ├── scrape\_services.py  
│       └── scrape\_faqs.py  
│  
├── frontend/  
│   ├── index.html                \# Chatbot UI  
│   ├── dashboard.html            \# Placement statistics page  
│   ├── admissions.html  
│   ├── courses.html  
│   ├── fees.html  
│   ├── events.html  
│   ├── services.html  
│   ├── style.css                 \# UI styling  
│   └── script.js                 \# Frontend logic  
│  
└── README.md

**2 TECHNOLOGIES USED** 

| Layer | Technology |
| ----- | ----- |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Data | JSON (structured knowledge base) |
| Scraping | BeautifulSoup, Requests |
| API | REST (POST /chat) |
| Deployment |  Localhost |

**3 PSGRKCW CHATBOT ARCHITECTURE**

 **Work Flow**

User → Browser → JavaScript → Flask API → JSON Knowledge Base → Response → Browser

**Logic Architecture**

1. User types a question  
2. Frontend sends question to Flask API  
3. Flask searches structured JSON data  
4. Best keyword match is found  
5. Reply is returned to UI

**4 BACKEND EXECUTION PROCESS (STEP-BY-STEP) Step 1: Install Python**

Ensure Python 3.10+ is installed

python \--version

**Step 2: Create Virtual Environment (Optional but Recommended)**

python \-m venv venv  
venv\\Scripts\\activate

**Step 3: Install Dependencies**

Create backend/requirements.txt:

flask  
flask-cors  
beautifulsoup4  
requests

Install:

python.exe \-m pip install \--upgrade pip

pip install \-r requirements.txt

 **Step 4: Web Scraping (One-Time or Periodic)**

Run each scraper to collect website data:

**cd backend/scraper**

python scrape\_admissions.py  
python scrape\_courses.py  
python scrape\_fees.py  
python scrape\_placements.py  
python scrape\_events.py  
python scrape\_services.py  
python faq\_scraper.py

**python scrape.py**  
**python merge\_faqs.py**

Output: Clean structured JSON files stored in backend/data/

**Step 5: Verify JSON Format**

Each JSON file **must look like this**:

{  
  "question": "...",  
  "reply": "...",  
  "keywords": \["keyword1", "keyword2"\]  
}

❌ No plain text  
❌ No empty arrays

**Step 6: Start Flask Server**

cd backend

python nlp\_bert.py  
python nlp\_tfidf.py  
python app.py

Expected output:

Running on http://127.0.0.1:5000

**5 BACKEND FILE Structure**

**app.py**

* Loads all JSON files  
* Filters invalid data  
* Matches keywords  
* Returns best response  
* Prevents crashes

**data/\*.json**

* Domain-wise knowledge base  
* Easy future updates  
* No database required

**scraper/\*.py**

* Extracts public data  
* Converts to chatbot format  
* Ensures clean JSON output

**6 FRONTEND EXECUTION PROCESS**

**🔹 Step 1: Open Chatbot UI**

frontend/index.html

(No server needed – opens in browser)

 **Step 2: Ask Questions**

Examples:

* “What courses are offered?”  
* “What is the fee structure?”  
* “Who are the top recruiters?”  
* “How to apply for admission?”

**Step  3: ADD FAQs in  backend Vector Database with JSON**

Frontend/admin.html

![][image1]

**7 FRONTEND FILE Structure**

**index.html**

* Chat UI  
* Input box  
* Message area

**script.js**

* Sends POST request to Flask  
* Displays response dynamically

**style.css**

* Chat layout  
* Responsive design  
* College-themed UI

**Supported Domains**

general, admission, fees, courses, placement, hostel,  
transport, exam, facilities, events, support, greetings

**SAMPLE API TEST (POSTMAN)**

**URL**

POST http://127.0.0.1:5000/chat

**Body (JSON)**

{  
  "message": "What are the placement companies?"  
}

**Response**

{  
  "reply": "Top recruiters include TCS, Infosys, Wipro and Deloitte."  
}

 **ERROR HANDLING** 

✔ Invalid JSON ignored  
✔ String-only data skipped  
✔ No server crash  
✔ CORS enabled  
✔ Clean fallback message

**Benefits of PSGR Chatbot**

* Structured domain-wise chatbot  
* No dependency on college server  
* Fully local deployment  
* Easy to maintain and scale  
* Beginner-friendly \+ industry-grade

**FUTURE ENHANCEMENTS**

* TF-IDF / BERT semantic search  
* Fee calculator  
* Admin panel  
* Voice assistant  
* Docker deployment

**CONCLUSION** 

	This project implements a locally deployed AI-based college chatbot using Flask and structured JSON data. It retrieves accurate, domain-specific information through keyword matching and provides clear responses without modifying the college website infrastructure.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAH9CAIAAAAmjMlmAAAniElEQVR4Xu3dT4hk13XH8Vp4MctZOWPIIgJh1NCbARkkyEIaMMYGBaydC3phGisxgxfBICMP45UIuCmyMNpEHrSTA8aTxUDZ2cxAEMgQg2ZhGC1GtBEKDCaLQVZwoyhJ5f1/955z76t3X3f1rfvu98MPM6qqrq46VX1+/aq624v/+vPnhBBCyLQs9EmEEELIyNAihBBCpocWIYQQMj20CCGEkOmhRQghhEwPLUIIIWR6aBFCCCHTQ4sQQgiZHlqEEELI9NAihBBCpocWIYQQMj20CCGEkOmhRQghhEwPLUIIIWR6aBFCCCHTQ4sQQgiZHlqEEELI9NAihBBCpocWIYQQMj20CCGEkOmhRQghhEwPLUIIIWR6aBFCCCHTQ4sQQgiZHlqEEELI9NAihBBCpocWIYQQMj20CCGEkOmhRQghhEwPLUIIIWR6aBFCCCHTQ4sQQgiZHlqEEELI9NAihBBCpocWIYQQMj20CCGEkOmhRQghhEwPLUIIIWR69rpFPv/v//nf//2/DQBkr1iGxUrUezJ69rRF/nz23/QHAAjFYizWo96ZEbOnLUKFAIBTsR71zoyYfWyR4qhNjg0A0Nqrl7b2sUU4EAGAAXt1OLKPLSIHBgCw6c0ZK7QIAKRHb85YoUUAID16c8YKLQIA6dGbM1ZoEQBIj96csUKLAEB69OaMFVoEANKjN2es0CIAkB69OWOFFgGA9OjNGSu0CACkR2/OWKFFACA9enPGCi0CAOnRmzNWaBEASI/enLFCiwBAevTmjBVaBADSozdnrNAiAJAevTljhRYBgPTozRkrtAgApEdvzlihRQAgPXpzxgotAgDp0ZszVmgRAEiP3pyxQosAQHr05owVWgQA0qM3Z6zQIgCQHr05Y4UWAYD06M0ZK7QIAKRHb85YoUUAID16c8YKLQIA6dGbM1ZoEQBIj96csUKLAEB69OaMFVoEANKjN2es0CIAkB69OWOFFgGA9OjNGSu0CACkR2/OWKFFACA9enPGCi0CAOnRmzNWaBEASI/enLFCiwBAevTmjBVaBADSozdnrNAiAJAevTljZeYtcv/7Vxa9KzffkxfY4t6y/djlWp430enJQXOVh6tTeWZUn7z1YntvSy/feSIvMex0ddh86MHJtnv2eNVO4WD1WJ5pWh+1t8dHjXHCg/704d3V924cXOs/8OpfXv/W7TsfPDmTFwX2g96csTLrFvli3ZVA7cr378vLDMupRfob1njxrU/kZQbtR4uEPuhP319985r9EZaD79198oX8ICA6vTljZc4tcvaLV+VKWLz67mfyYkMyapFHt/6qva+tZ24/kpcashctEvagP10fDzVI64XVI4oEe0ZvzliZcYucvfvtZglcOTruVsurvwh5jWIHLbKnfn/rmeae3jj+bvvPv7oVUiM7bpGjMY9A0IP+9O53jNe+nn31rQenT+sLfvbkg3eO2ymUDv4hZBLA7unNGSvzbZHP3v1WswGu3HyvXy4DL/c/fe+t5fNX60tdfX751ntPHS3Sr7/l+oun7/9seb3+iC9dvd699PGf76++/Uy9n64+9+qquB6D61ik37/Le5uzx3d/+PLB1S/VH3/w6u37l/CKygdvtN+TF/PpG8X/psLZ6d2/v9HcySvP3Pj7u6dn3hap7lF72Wdv/PCXp2c7apGgB72/m4vF866jjQ9X17sLDBzQADHozRkrs22RJ2/faL78r9x8v/jvBzfbbzvdL/c/OjE2RuvFF7q3CnSLHLz4Qntm6+rR+umHd240TdSffPzr/nvh4RY5+Lr66EW547Z9b39O73fTufF2sW+fvNXeNfebCk/XS30rr714vW0is0We3nNd9oX+shfYIkEPel+ci2du/V6eW3vys/4HDoqCB/aH3pyxMtcWMfbgD8p9svnifrdRHC/3v3dTbzqbbhGnK1edV2R8LzzcIh7+Y4IL0W/bG/UNNban/h78yZ2X2zM9+hb55E67130usEWCHnTjXjz3pnpCtIyHe/vLdMAl0pszVmbaIv0Prfb79/0ftBtFvtxvvPSxeOb4l4/OvigW0Nmjd141GsHZItdvPSh/FPTs92+aBzJXv33ntDz19M4r3cvu/dsqW1vkme/effRZeQM++Mcb3cfvdIX1Pxrbtd2TfvvLNxWMF4Kufn11v/pZ2LMn9289355q3NpHt/vL3jhpL/vgljGu0S3iZL61HvagP3rzufZKhvrJ+ImvoYsBl01vzliZZ4v030rXr2zUfnerfQlDfGu/Pm4XhVjWxm8eOFrkxZ91BxjGN7ZXbt7vXmHXb6tsbZEX3jJewf+gu8U7bBHjG/bq5aza2buvtDfJflPh9B/bCriy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>