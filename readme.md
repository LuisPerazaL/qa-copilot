# 🤖 QA Copilot

An AI-powered command-line tool that automatically generates detailed test cases from software requirements and user stories using the Gemini API.

## 📋 Overview

QA Copilot takes a requirement ID and a user story as input, sends them to Google's Gemini AI, and returns fully structured test cases including steps, preconditions, and expected results — ready to export as CSV.

This eliminates hours of manual test case writing and ensures consistent, professional QA documentation.

---

## 🏗️ Architecture

```
qa-copilot/
├── main.py          # CLI menu and user interaction
├── generator.py     # Gemini API integration & test case generation
├── exporter.py      # CSV export logic
├── test_case.py     # TestCase data model
├── .env             # API key (not committed to git)
└── test_cases.csv   # Generated output
```

### Flow

```
User Input (Req ID + User Story)
        ↓
   generator.py
        ↓
  Gemini AI API  →  JSON Response
        ↓
  Parse & build TestCase objects
        ↓
  Display in terminal / Export to CSV
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/qa-copilot.git
cd qa-copilot
```

### 2. Install dependencies

```bash
pip install google-genai python-dotenv
```

### 3. Get your Gemini API key

- Go to [aistudio.google.com](https://aistudio.google.com)
- Click **Get API Key** → Create a new key (free, no credit card required)

### 4. Configure your API key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your-api-key-here
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

---

## 🚀 Usage

```bash
python main.py
```

You'll see the main menu:

```
===== QA COPILOT =====
1. Create Test Cases (AI-powered)
2. View Test Cases
3. Export CSV
4. Exit
```

**Option 1** — Enter a Requirement ID and User Story. Gemini AI generates 4–6 detailed test cases.

**Option 2** — View the generated test cases in the terminal.

**Option 3** — Export all test cases to `test_cases.csv`.

---

## 📊 Generated Test Case Fields

| Field | Description |
|---|---|
| ID | Unique identifier (TC001, TC002...) |
| Title | Short descriptive name |
| Type | Positive / Negative / Edge |
| Priority | High / Medium / Low |
| Preconditions | What must be true before running the test |
| Steps | Numbered, actionable steps |
| Expected Result | What success looks like |

---

## 🧪 Example

**Input:**
```
Requirement ID: SA6-14938
User Story: The calculadora_simulador component must initialize and run
at least 2 worker threads in parallel...
```

**Output (CSV excerpt):**
```
TC001 | Successful concurrent execution with multiple workers | Positive | High
TC002 | One worker failing with correct DB error logging     | Negative | High
TC003 | Minimum 2 concurrent workers execute successfully    | Edge     | High
```

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Google Gen AI SDK** (`google-genai`) — Gemini 2.5 Flash model
- **csv** — Standard library for export
- **python-dotenv** — Secure API key management

---

## 🔮 Future Improvements

- [ ] Persist test cases between sessions (JSON/SQLite)
- [ ] Web interface with Flask or Streamlit
- [ ] Export to XLSX with formatting
- [ ] Support for Jira/TestRail integration
- [ ] Multi-language support (Spanish/English)

---

## 👤 Author

Built as a final project for **Stanford University** — demonstrating practical AI integration in software quality assurance workflows.