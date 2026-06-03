# QA Copilot 🤖

QA Copilot is an AI-powered assistant that helps QA Engineers generate structured test cases from software requirements and user stories.

<img width="1906" height="921" alt="image" src="https://github.com/user-attachments/assets/36a54e65-02fa-49dc-9a15-12349e54e9f1" />
<img width="1915" height="948" alt="image" src="https://github.com/user-attachments/assets/0d8cc625-cfd3-4dc1-a2fe-19d7e716306b" />
<img width="1915" height="952" alt="image" src="https://github.com/user-attachments/assets/97ccfd20-d596-46c8-aa90-4d34e11b0357" />




Built with Python and Streamlit, the application accelerates test design by creating comprehensive test scenarios inspired by ISTQB testing techniques.

## Features

* Generate test cases from requirements and user stories
* Supports:

  * Functional Testing
  * Negative Testing
  * Boundary Testing
  * Security Testing
  * Performance Testing
  * Data Validation
* Export results to CSV
* Export results to Excel
* Test case history tracking
* Streamlit-based web interface
* Demo Mode support

## Tech Stack

* Python
* Streamlit
* Pandas
* OpenPyXL
* AI Provider (Gemini, DeepSeek, or compatible LLM)

## Installation

Clone the repository:

```bash
git clone https://github.com/LuisPerazaL/qa-copilot.git
cd qa-copilot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run App.py
```

or

```bash
python -m streamlit run App.py
```

The application will be available at:

```text
http://localhost:8501
```

## Demo Mode

If an AI provider is unavailable or API credits have been exhausted, QA Copilot can run in Demo Mode.

Windows:

```bash
set QA_COPILOT_DEMO=1
```

Linux / macOS:

```bash
export QA_COPILOT_DEMO=1
```

Then run the application normally.

## Environment Variables

Example:

```bash
DEEPSEEK_API_KEY=your_api_key
```

or

```bash
GOOGLE_API_KEY=your_api_key
```

## Example User Story

Requirement ID:

```text
BANK-TRF-001
```

User Story:

```text
As a banking customer, I want to transfer money to third-party accounts so that I can send funds securely and efficiently.
```

QA Copilot generates structured test cases covering positive, negative, security, boundary, and performance scenarios.

## Future Enhancements

* Gherkin / BDD support
* Playwright test generation
* Risk-based test prioritization
* Requirement ambiguity detection
* API test case generation

## Author

Luis Peraza

Final project developed during Stanford Code in Place 2026 under the guidance of Section Leader Sumaiya Islam.
