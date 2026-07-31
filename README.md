# 🎓 CampusPilot AI – Agentic AI Powered Smart Campus Management System

<p align="center">
  <img src="https://img.icons8.com/color/144/graduation-cap.png" width="120"/>
</p>

<p align="center">
  <b>An AI-powered campus management platform that helps students organize their academic journey through intelligent planning, task management, career guidance, placement tracking, and AI assistance.</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

</p>

---

# 📖 Overview

CampusPilot AI is an **Agentic AI-powered Smart Campus Management System** developed to simplify student life by bringing multiple academic activities into one intelligent platform.

The application enables students to manage their profiles, generate personalized study plans, organize assignments, maintain timetables, explore placement opportunities, receive AI-powered career guidance, track campus events, and interact with an intelligent AI assistant.

Instead of switching between multiple applications, students can perform all essential academic tasks from a single platform.

---

# ✨ Key Features

### 👤 Student Profile

* Create and manage student information
* Department & academic details
* Contact information
* Profile management

---

### 📚 AI Study Planner

* Personalized study plans
* Subject-wise preparation schedule
* Daily study hour planning
* Difficulty-based recommendations
* Gemini AI generated study roadmap

---

### 📝 Assignment Manager

* Add assignments
* Track pending work
* Organize deadlines
* Academic task management

---

### 📅 Smart Timetable

* Weekly timetable management
* Subject scheduling
* Organized daily routine
* Easy timetable updates

---

### 💼 Placement Hub

* Placement preparation resources
* Company information
* Interview preparation
* Placement tracking

---

### 🎯 AI Career Guide

* Career recommendations
* Skill improvement suggestions
* Industry guidance
* Learning roadmap

---

### 📢 Campus Events

* Manage college events
* Track upcoming activities
* Academic announcements
* Event organization

---

### 🤖 AI Assistant

* Gemini AI powered chatbot
* Academic question answering
* Student assistance
* Intelligent recommendations

---

### 🌙 Dark / Light Theme

* Modern UI
* User-friendly experience
* Theme switching support

---

# 🏗️ System Architecture

```text
                CampusPilot AI

                    │
                    ▼
             Streamlit Frontend
                    │
                    ▼
             Workflow Controller
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
   AI Services              Database Layer
      │                           │
      ▼                           ▼
 Gemini AI API             SQLite Database
      │
      ▼
 Intelligent Responses
```

---

# 🛠️ Tech Stack

| Category    | Technologies               |
| ----------- | -------------------------- |
| Frontend    | Streamlit                  |
| Backend     | Python                     |
| Database    | SQLite                     |
| AI Model    | Google Gemini AI           |
| API         | Gemini API                 |
| ORM         | SQLAlchemy                 |
| Environment | Python Virtual Environment |
| IDE         | Visual Studio Code         |

---

# 📂 Project Structure

```text
CampusPilot-AI/

├── app.py
├── database/
├── services/
├── ui/
│   ├── dashboard.py
│   ├── profile.py
│   ├── study.py
│   ├── assignment.py
│   ├── placement.py
│   ├── timetable_page.py
│   ├── career_page.py
│   ├── event_page.py
│   ├── ai_chat.py
│   └── components/
├── assets/
├── models/
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/CampusPilot-AI.git
```

---

### Move into Project

```bash
cd CampusPilot-AI
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Run Application

```bash
streamlit run app.py
```

---

# 📸 Application Modules

* 🏠 Dashboard
* 👤 Student Profile
* 📚 Study Planner
* 📝 Assignments
* 📅 Timetable
* 💼 Placement Hub
* 🎯 Career Guide
* 📢 Events
* 🤖 AI Assistant
* 🌙 Dark/Light Theme

---

# 🎯 Future Enhancements

* 🔐 User Authentication
* 👨‍🏫 Faculty Dashboard
* 🏫 Admin Panel
* ☁️ Cloud Database Integration
* 📧 Email Notifications
* 📱 Mobile Application
* 🔔 Smart Deadline Reminders
* 📊 Advanced Analytics Dashboard
* 📂 File Upload Support
* 🤖 AI-Based Automatic Task Tracking

---

# ⚠️ Current Limitations

* Assignment completion is updated manually by the user.
* Campus events require manual entry.
* SQLite is intended for small-scale deployments.
* No multi-user authentication in the current version.
* AI responses depend on the configured Gemini API.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

### **Darshan S**

**B.Tech – Artificial Intelligence & Data Science**

**Prathyusha Engineering College**

**Linkedin -**  www.linkedin.com/in/darshans27

**Github -**  https://github.com/darshan468

Passionate about building AI-powered software solutions that improve productivity and solve real-world problems.

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates future improvements.

> **CampusPilot AI — Empowering Students with Agentic AI for Smarter Campus Management.**
