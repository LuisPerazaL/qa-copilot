# QA Copilot 🤖

An AI-driven QA aid for creating well-organized test cases from software needs and user narratives.

Developed using Python and Streamlit, QA Copilot empowers QA Engineers to speed up test plan creation. it makes structured test cases based on testing methods inspired by ISTQB.

## Capabilities

Test cases generation from specifications and user narratives.
Comprehends:

Functional Testing
Negative Testing
Boundary Testing
Security Testing
Performance Testing
Data Validation
Results export to CSV is provided.
Results can be exported to Excel too.
Tracking of test case historical data.
A Streamlit web interface is available.
Support for a demo mode.

## Technology Core

Python
Streamlit
Pandas
OpenPyXL
An AI Provider (Gemini DeepSeek or a similar LLM)

## Setup

Copy the repository:

```bash
git clone https://github. com/LuisPerazaL/qa-copilot. git
cd qa-copilot
```

Make and activate a virtual space:

```bash
python -m venv . venv
```

For Windows systems:

```bash
. venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements. txt
```

## Executing the Program

```bash
streamlit run App. py
```

Alternatively you can use:

```bash
python -m streamlit run App. py
```

The app you will find at:

```text
http://localhost:8501
```

## Demo Operation

If an AI source is out of reach or its credits are all used up QA Copilot can operate in Demo Mode. Forcing Demo Mode:

Windows:

```bash
set QA_COPILOT_DEMO=1
```

Linux or macOS systems:

```bash
export QA_COPILOT_DEMO=1
```

Next launch the application as usual.

```bash
streamlit run App. py
```

## Environment Variables Setting

Such as:

```bash
DEEPSEEK_API_KEY=your_api_key
```

Or perhaps:

```bash
GOOGLE_API_KEY=your_api_key
```

## A User Story Example

Requirement ID's name:

```text
BANK-TRF-001
```

User Story presented:

```text
As a banking customer, I want to transfer money to third-party accounts so that I can send funds securely and efficiently.
```

QA Copilot its self will create organized test cases with positive, negative, security, boundary and performance situations.

## Upcoming Enhancements

Gherkin or BDD framework assistance
Playwright test creation abilities
Risk factor based test sequencing
Identifying unclear requirements
Generating API test instances

## Creator

Luis Peraza

This final project was made during Stanford Course at SL Sumaiya Islam.
