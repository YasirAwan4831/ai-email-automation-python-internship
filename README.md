<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=📧%20Email%20Automation%20System&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Professional%20Python%20Email%20Automation%20with%20Gmail%20API&descAlignY=55&descSize=16" width="100%"/>

<br/>

<!-- STATUS BADGES -->
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gmail API](https://img.shields.io/badge/Gmail%20API-Integrated-EA4335?style=for-the-badge&logo=gmail&logoColor=white)
![OAuth](https://img.shields.io/badge/OAuth-2.0-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-✅%20Working-22c55e?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Internship](https://img.shields.io/badge/AI%20Internship-Nest--Agent-8b5cf6?style=for-the-badge&logo=sparkles&logoColor=white)

<br/><br/>

<!-- TYPING ANIMATION -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=4F8EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=60&lines=Send+%7C+Schedule+%7C+Automate+Emails+%F0%9F%9A%80;Built+with+Python+%2B+Gmail+API+%F0%9F%94%90;Secure+OAuth+2.0+Authentication+%E2%9C%85" alt="Typing SVG" />

<br/><br/>

<a href="#-installation"><img src="https://img.shields.io/badge/🚀%20Get%20Started-2563eb?style=for-the-badge"/></a>
&nbsp;
<a href="#-features"><img src="https://img.shields.io/badge/✨%20Features-7c3aed?style=for-the-badge"/></a>
&nbsp;
<a href="#-tech-stack"><img src="https://img.shields.io/badge/🛠️%20Tech%20Stack-0f766e?style=for-the-badge"/></a>

</div>

---

## 🌟 Overview

The **Email Automation System** is a professional Python-based automation project developed to send, schedule, and manage emails efficiently using the Gmail API.

> 💡 Developed as part of an **AI Internship Project** at **Nest-Agent** — demonstrating real-world API integration, OAuth authentication, and automation workflows.

<table>
<tr>
<td>

**What it does:**
- 📩 Gmail API Integration
- ⏰ Email Scheduling
- 🎨 HTML Email Templates
- 🧾 Email Logging System

</td>
<td>

**How it works:**
- 🔐 OAuth Authentication
- ⚙️ Automation Workflows
- 🛡️ Secure Email Handling
- 📂 Modular Architecture

</td>
</tr>
</table>

---

## ✨ Features

<div align="center">

| Feature | Description | Status |
|:-------:|:-----------|:------:|
| 📩 Instant Sending | Send emails immediately via Gmail API | ✅ |
| ⏰ Scheduling | Auto-deliver emails at set times | ✅ |
| 🔐 OAuth 2.0 | Secure Google authentication, no password stored | ✅ |
| 🧾 Logging | Full email history with timestamps | ✅ |
| 🎨 HTML Templates | Beautiful, customizable email designs | ✅ |
| 📂 Modular Code | Clean, maintainable project structure | ✅ |
| ⚡ Lightweight | Fast performance, minimal dependencies | ✅ |
| 🖥️ Terminal UI | Interactive menu-driven interface | ✅ |

</div>

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-Core%20Backend-3776AB?style=flat-square&logo=python&logoColor=white)
![Gmail API](https://img.shields.io/badge/Gmail%20API-Email%20Sending-EA4335?style=flat-square&logo=gmail&logoColor=white)
![OAuth 2.0](https://img.shields.io/badge/OAuth%202.0-Authentication-4285F4?style=flat-square&logo=google&logoColor=white)
![Schedule](https://img.shields.io/badge/Schedule%20Lib-Task%20Scheduling-22c55e?style=flat-square&logo=clockify&logoColor=white)
![Dotenv](https://img.shields.io/badge/Dotenv-Env%20Variables-eab308?style=flat-square&logo=dotenv&logoColor=white)
![HTML CSS](https://img.shields.io/badge/HTML%2FCSS-Email%20Templates-e11d48?style=flat-square&logo=html5&logoColor=white)

</div>

---

## 📁 Project Structure

```
📦 email-automation-system/
│
├── 📁 logs/
│   └── 📄 email_logs.txt          ← all sent email records
│
├── 📁 templates/
│   └── 🎨 email_template.html     ← HTML email design
│
├── 📁 utils/                      ← helper utilities
│
├── 📁 .venv/                      ← virtual environment
│
├── 🔒 .env                        ← secrets (never commit!)
├── ⚙️  config.py                   ← configuration settings
├── 📧 email_service.py            ← core email logic
├── 📝 logger.py                   ← logging system
├── 🚀 main.py                     ← entry point
├── ⏰ scheduler.py                ← scheduling logic
├── 📦 requirements.txt
├── 🔑 credentials.json            ← OAuth credentials (never commit!)
├── 🔑 token.json                  ← OAuth token (never commit!)
└── 📖 README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-automation-system.git
cd email-automation-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

**Activate:**

```bash
# Windows
.\.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Gmail API Setup

### Step 1 — Open Google Cloud Console

👉 [https://console.cloud.google.com/](https://console.cloud.google.com/)

### Step 2 — Create a Project

Create a new project and name it:
```
Email Automation System
```

### Step 3 — Enable Gmail API

```
APIs & Services → Library → Gmail API → Enable
```

### Step 4 — Configure OAuth Consent Screen

```
APIs & Services → OAuth Consent Screen
```

Configure:
- **App Type:** External
- **App Name:** Email Automation System
- **Support Email:** your Gmail
- **Test Users:** add your Gmail

### Step 5 — Create OAuth Credentials

```
APIs & Services → Credentials → Create Credentials → OAuth Client ID → Desktop App
```

Download the JSON file → Rename to `credentials.json` → Place in project root.

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
# Email Configuration
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_password_here

# Time Zone
TZ=UTC
```

> ⚠️ **Never commit this file to GitHub!**

---

## ▶️ Run The Project

```bash
python main.py
```

---

## 🖥️ Application Menu

```
╔══════════════════════════════════════╗
║     📧 Email Automation System       ║
╠══════════════════════════════════════╣
║  1.  Send an email immediately       ║
║  2.  Schedule an email               ║
║  3.  Start scheduler loop            ║
║  4.  Exit                            ║
╚══════════════════════════════════════╝
```

---

## 🎨 HTML Email Templates

Templates are stored in `templates/email_template.html`. You can customize:

| Element | What to Change |
|---------|---------------|
| 🎨 Colors | Brand color scheme |
| 🖼️ Logo | Company logo URL |
| 🏢 Company Name | Header/footer text |
| 🔘 Buttons | CTA button text & links |
| 📐 Layout | Section arrangement |

**Adding a logo:**
```html
<img src="YOUR_IMAGE_URL" alt="Company Logo" width="150">
```

Host images on: GitHub · ImgBB · Cloudinary · Your website

---

## 🧾 Logging System

Every email is automatically logged in `logs/email_logs.txt`:

```
[2024-12-15 09:32:11] | TO: client@company.com | SUBJECT: Q4 Report | STATUS: ✅ SENT
[2024-12-15 10:15:44] | TO: team@nestAgent.io  | SUBJECT: Reminder   | STATUS: ✅ SENT
[2024-12-15 11:00:02] | TO: invalid@noDomain   | SUBJECT: Test       | STATUS: ❌ FAILED
```

---

## 🔒 Security Notes

> ⚠️ **Never push these files to GitHub!**

```gitignore
# Add to .gitignore
.env
credentials.json
token.json
```

| File | Why It's Sensitive |
|------|-------------------|
| `.env` | Contains email credentials |
| `credentials.json` | Google OAuth app secrets |
| `token.json` | Your personal access token |

---

## 🧠 Authentication Flow

```
Run python main.py
        ↓
First run detected?
        ↓
Browser opens → Google OAuth Login
        ↓
Grant Gmail permissions
        ↓
token.json saved automatically
        ↓
✅ Ready! No re-login needed.
```

---

## 🚀 Future Improvements

<div align="center">

| # | Feature | Priority |
|:-:|:--------|:--------:|
| 1 | 🖥️ GUI Interface | 🔴 High |
| 2 | 🤖 AI Generated Emails | 🔴 High |
| 3 | 📨 Bulk Email Sending | 🟡 Medium |
| 4 | 📊 Email Analytics Dashboard | 🟡 Medium |
| 5 | 📎 Attachment Support | 🟡 Medium |
| 6 | 👥 Multi-user Support | 🟢 Low |
| 7 | 🌐 Web Dashboard | 🟢 Low |

</div>

---

## 🤝 Developer

<div align="center">

<img src="https://img.shields.io/badge/Developed%20by-Muhammad%20Yasir-4f8ef7?style=for-the-badge&logo=github"/>

**Muhammad Yasir**
AI Intern @ Nest-Agent

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/yasirawan4831/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/YasirAwan4831)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify and distribute.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&animation=twinkling" width="100%"/>

###  Thank You For Visiting This Project!

⭐ **If you found this useful, please star the repository!** ⭐

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasir.email-automation-system&left_color=gray&right_color=blue)
&nbsp;
![Made with Love](https://img.shields.io/badge/Made%20with-YasirAwan-red?style=flat-square)
&nbsp;
![Nest-Agent](https://img.shields.io/badge/Nest--Agent-AI_Automation%20Internship-8b5cf6?style=flat-square)

</div>