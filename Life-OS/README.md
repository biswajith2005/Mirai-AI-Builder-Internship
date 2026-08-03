# 🧠 Life-OS: AI Wellbeing Dashboard

> **An AI-powered digital wellbeing dashboard that transforms screen time data into actionable lifestyle coaching using Google Gemini.**

---

## 📌 Overview

**Life-OS** is a Streamlit-based dashboard designed to help users understand and improve their digital habits. It analyzes daily screen time usage, visualizes trends, and leverages Google's Gemini AI to provide personalized productivity and wellbeing recommendations.

Instead of simply telling users to "use your phone less," Life-OS identifies unhealthy usage patterns and recommends practical real-world activities such as exercising, reading, meal prepping, and spending time outdoors.

---

## ✨ Features

* 📊 **Screen Time Analytics**

  * Visualizes 14 days of screen time data.
  * Tracks app usage across different categories.

* 📈 **Interactive Dashboard**

  * Daily screen time metrics.
  * Most-used app analysis.
  * Daily goal tracking with progress indicators.
  * Interactive charts and visualizations.

* 🤖 **AI Lifestyle Coach**

  * Powered by **Google Gemini 2.5 Flash**.
  * Analyzes screen time habits.
  * Generates personalized productivity insights.
  * Suggests healthy offline alternatives.
  * Provides motivational coaching.

* 🎭 **Guilt-Trip Avatar (Innovation Feature)**

  * AI generates a symbolic image representing your digital habits.
  * Uses Polinations AI image generation.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* Google Gemini API (`google-genai`)
* Python Dotenv
* Polinations AI

---

## 📂 Project Structure

```text
Life-OS/
│
├── app.py
├── screentime.csv
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### Navigate to the project

```bash
cd Life-OS
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

## 📊 Dataset

The application uses a synthetic **14-day screen time dataset** containing:

* Date
* App Name
* Category
* Minutes Used

Categories include:

* Social Media
* Entertainment
* Education
* Coding
* Career

---

## 🧠 AI Workflow

```text
Screen Time CSV
        │
        ▼
Pandas Data Processing
        │
        ▼
Category Summary
        │
        ▼
Google Gemini AI
        │
        ├────────────► Personalized Coaching
        │
        ▼
AI Image Prompt
        │
        ▼
Polinations AI
        │
        ▼
Dynamic Avatar
```

---

## 📸 Dashboard Highlights

* Daily KPI Cards
* Goal Progress Tracking
* 14-Day Trend Analysis
* Category Distribution Charts
* AI Productivity Coaching
* AI Reflection Avatar

---

## 🎯 Learning Outcomes

This project demonstrates:

* Data Visualization
* Streamlit Dashboard Development
* Prompt Engineering
* Generative AI Integration
* API Integration
* Data Processing with Pandas
* UI Design for Analytics Applications

---

## 👨‍💻 Author

**Bathula Biswajith Yadav**

B.Tech Computer Science Engineering

MirAI School of Technology – Virtual Summer Internship 2026

---

## 📄 License

This project was developed as part of the **MirAI School of Technology Virtual Summer Internship 2026 – AI Builder Track** for educational purposes.
