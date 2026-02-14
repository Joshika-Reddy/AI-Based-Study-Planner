# 📘 AI Study Planner

A simple AI-based web application that generates a personalized daily study plan based on subjects, marks, and difficulty level. The app intelligently distributes study hours and visualizes the plan using charts.

---

## 🚀 Features
- Add multiple subjects dynamically
- Enter current marks for each subject
- Select difficulty level (Easy / Medium / Hard)
- Enter total available study hours per day
- Automatically generates optimized study plan
- Displays study hours using a bar chart visualization

---

## 🧠 How it works
Priority = (100 - Marks) × Difficulty Weight

Difficulty weights:
- Easy → 1  
- Medium → 2  
- Hard → 3  

Subjects with lower marks and higher difficulty get more study hours.

---

## 🛠️ Tech Stack
- Python (Flask)
- HTML & CSS
- Chart.js

---

## 💻 Run Locally
1. Clone repo  
git clone https://github.com/Joshika-Reddy/AI-Based-Study-Planner.git

2. Install Flask  
pip install flask

3. Run app  
python ai-study-planner.py

4. Open browser  
http://127.0.0.1:5000/

---

## 👩‍💻 Author
Joshika Reddy – CSE (AI & ML)
