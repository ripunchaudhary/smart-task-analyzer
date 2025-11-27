# 🧠 SMART TASK ANALYZER  
A Django REST + JavaScript based system that analyzes tasks, calculates priority scores, and recommends the top 3 tasks to focus on using predefined productivity strategies.

This project is submitted as part of the Internshive Internship Assignment 2025.

---

# 📌 1. PROBLEM STATEMENT  
Managing tasks manually becomes difficult when deadlines, effort, dependencies, and importance overlap.  
The goal of this assignment is to build a system that can:

- Accept a list of tasks  
- Analyze each task using a scoring algorithm  
- Support multiple strategies (fastest, impact, deadline, smart)  
- Return sorted tasks by priority  
- Suggest the top 3 tasks with reasoning  
- Provide a frontend interface for easy testing  

---

# 📌 2. FEATURES 

✔ Analyze API – Returns full priority ranking  
✔ Suggest API – Returns top 3 tasks with reasons  
✔ Custom scoring algorithm  
✔ 4 strategies (fastest, impact, deadline, smart)  
✔ Weighted scoring system  
✔ Color-coded frontend UI  
✔ CORS enabled  
✔ JSON validation  
✔ Unit tests  
✔ Full documentation  

---

# 📌 3. PROJECT STRUCTURE

```
task-analyzer/
│
├── backend/
│   ├── task_analyzer/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── tasks/
│   │   ├── scoring.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── manage.py
│   ├── db.sqlite3
│   └── venv/
│
└── frontend/
    ├── index.html
    ├── styles.css
    └── script.js


---

# 📌 4. BACKEND SETUP (Django)

 1️⃣ Create virtual environment

cd backend
python -m venv venv


2️⃣ Activate environment  

venv\Scripts\activate


3️⃣ Install dependencies

pip install django djangorestframework django-cors-headers

4️⃣ Run backend

python manage.py runserver


Backend URL:

http://127.0.0.1:8000/


---

# 📌 5. FRONTEND SETUP

Open `frontend/index.html` using Live Server

Frontend URL:

http://127.0.0.1:5500/


Paste JSON → Select Strategy → Click Analyze → See results.

---

# 📌 6. API ENDPOINTS

---

1️⃣ Analyze Tasks API

POST /api/tasks/analyze/?strategy=smart


### Request JSON:
[
  {
    "task_id": "t1",
    "title": "Fix login bug",
    "due_date": "2025-11-30",
    "estimated_hours": 3,
    "importance": 8,
    "dependencies": []
  }
]


### Response:
[
  {
    "task_id": "t1",
    "title": "Fix login bug",
    "score": 0.719,
    "urgency": 0.90,
    "importance": 0.80,
    "effort": 0.63,
    "dependency": 0.20
  }
]


---

2️⃣ Suggest Top Tasks API

POST /api/tasks/suggest/?strategy=smart


## Response:
[
  {
    "task_id": "t1",
    "title": "Fix login bug",
    "score": 0.719,
    "reason": "Urgency: 0.90, Importance: 0.80, Effort: 0.63, Dependency: 0.20"
  }
]

---

# 📌 7. SCORING ALGORITHM (Detailed Explanation)

Each task is analyzed using **4 key metrics**:

1️⃣ Urgency Score
Based on remaining days:

urgency = 1 - (days_left / 30)

- No due date → urgency = 0.3  
- Overdue → urgency = 1  

---

2️⃣ Importance Score

User input /10:
importance = importance_value / 10

---

3️⃣ Effort Score
Less hours → higher score:

effort = 1 - min(hours / 8, 1)

---

4️⃣ Dependency Score
If task blocks others:

dependency = blockers_count / 5

---

 ⭐ FINAL SCORE

score =
(urgency * w_u) +
(importance * w_i) +
(effort * w_e) +
(dependency * w_d)


---

# 📌 8. STRATEGY WEIGHTS


fastest  → prioritizes low effort tasks  
impact   → prioritizes high importance tasks  
deadline → prioritizes urgency  
smart    → balanced weighting  


# Strategy weight matrix:

{
  "fastest": {"w_u": 0.1, "w_i": 0.2, "w_e": 0.6, "w_d": 0.1},
  "impact":  {"w_u": 0.15, "w_i": 0.7, "w_e": 0.05, "w_d": 0.1},
  "deadline":{"w_u": 0.7, "w_i": 0.1, "w_e": 0.05, "w_d": 0.15},
  "smart":   {"w_u": 0.35, "w_i": 0.35, "w_e": 0.15, "w_d": 0.15}
}

---

# 📌 9. UNIT TESTING 


backend/tasks/tests.py

Covers:

✔ Urgency calculation
✔ Effort calculation
✔ Score sorting
✔ Strategy behavior
✔ API outputs 

# Run tests

python manage.py test

---

# 📌 10. SAMPLE JSON FOR TESTING

[
  {
    "task_id": "t1",
    "title": "Fix payment gateway",
    "due_date": "2025-11-29",
    "estimated_hours": 4,
    "importance": 9,
    "dependencies": []
  },
  {
    "task_id": "t2",
    "title": "Design landing page",
    "due_date": "2025-12-10",
    "estimated_hours": 6,
    "importance": 6,
    "dependencies": []
  }
]

---

 📌 11. TIME BREAKDOWN (As required)

| Activity      | Time   |
|---------------|--------|
| Backend setup | 1 hr   |
| Scoring logic | 2 hr   |
| Analyze API   | 45 min |
| Suggest API   | 45 min |
| Frontend      | 1.5 hr |
| Debugging     | 1 hr   |
| Documentation | 45 min |

---

 📌 12. CHALLENGES

- CORS configuration issues
- Normalizing scoring factors
- Handling missing due dates
- Multi-strategy fine-tuning
- API + frontend connection 

---

 📌 13. FUTURE IMPROVEMENTS

- User login system  
- Task categories  
- Calendar integration  
- Machine-learning prioritization  
- Team collaboration mode  

---

 📌 14. CONCLUSION

This project successfully implements:

✔ Task Analysis  
✔ Task Suggestion  
✔ Fully working scoring algorithm  
✔ Multiple strategies  
✔ Frontend interface  
✔ Proper backend structure  
✔ Full documentation  
✔ All assignment requirements  
---

Run the Backend
cd backend
venv\Scripts\activate
python manage.py runserver

---
![Screenshot](assest/Img1.png)
![Screenshot](assest/Img2.png)



