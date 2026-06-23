# 🚀 AI-Powered App Builder

An intelligent system that automatically generates application structure (UI, APIs, database, and workflows) from a simple natural language description.

---

## 📌 Overview

The **AI-Powered App Builder** converts user prompts into a complete app blueprint using an AI-driven pipeline.
It simulates real-world AI systems with features like intent detection, design generation, validation, and auto-repair.

---

## ✨ Features

* 🧠 **Intent Detection**
  Extracts entities, features, and roles from user input

* 🏗 **Design Generation**
  Creates modules and user flow automatically

* 📊 **Schema Generation**
  Generates UI structure, APIs, and database schema

* ⚠️ **Validation Engine**
  Detects missing APIs and inconsistencies

* 🔧 **Auto Repair System**
  Fixes errors like missing endpoints

* 📈 **Execution Metrics**
  Tracks success, failures, and repairs

---

## 🛠 Tech Stack

* **Python 3.13**
* **Streamlit** (UI)
* **Custom AI Pipeline**
* Optional: **Google Gemini API** (for real AI integration)

---

## 📂 Project Structure

```
AI-App-Builder/
│── app.py
│── pipeline/
│   ├── intent.py
│   ├── design.py
│   ├── schema.py
│   ├── validate.py
│   ├── repair.py
│   └── execute.py
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install streamlit
```

### 2. Run the app

```
python -m streamlit run app.py
```

---

## 💡 Example Prompt

```
Build a CRM with login, contacts, dashboard, role-based access, and payment integration.
```

---

## 📸 Output Includes

* Intent (entities, features, roles)
* System design
* API + Database schema
* Validation errors (if any)
* Auto-repaired schema
* Execution results

---

## 🔄 AI Modes

* ✅ **Fallback AI (Default)** – Works without API
* 🔥 **Hybrid Mode** – Uses Gemini API + fallback
* 🚀 **Full AI Mode** – Requires valid API key

---

## 🎯 Use Cases

* Academic projects
* AI system demonstrations
* Rapid prototyping
* Learning system design

---

## 📊 Sample Metrics

```
Total Requests: 1  
Success: 1  
Failures: 0  
Repairs: 1  
```

---

## 🚀 Future Enhancements

* Code generation (React / Flask)
* Deployment support
* Advanced UI (ChatGPT-like interface)
* Multi-model AI integration

---

## 👨‍💻 Author

Developed as an AI-based system design project by Diyakrishna

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share with others
* Contribute improvements

---
