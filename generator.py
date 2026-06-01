import os
import json
from google import genai
from test_case import TestCase
from demo_data import get_demo_test_cases


def generate_test_cases(requirement_id, user_story, demo_mode=False, **kwargs):
    api_key = os.environ.get("GOOGLE_API_KEY")

    if demo_mode or not api_key:
        return get_demo_test_cases(user_story)

    client = genai.Client(
        api_key=api_key
    )

    prompt = f"""You are a Senior QA Engineer with strong ISTQB knowledge.
    Analyze the requirement and generate a comprehensive test suite that maximizes test coverage.
    With 10 years of experience, you excel at creating clear, concise, and actionable test cases that cover all relevant scenarios.

Requirement ID: {requirement_id}
User Story: {user_story}

Return ONLY a valid JSON object with the following structure:

{{
  "test_cases": [
    {{
      "tc_id": "TC001",
      "title": "Short descriptive title",
      "tc_type": "Functional",
      "priority": "High",
      "preconditions": "Required setup",
      "steps": [
        "Step 1: description",
        "Step 2: description"
      ],
      "expected_result": "Expected behavior"
    }}
  ]
}}

Rules:

- Generate a comprehensive test suite of approximately 100 distinct test cases whenever the requirement supports it.
- When the user story references business domains such as finance, banking, payments, loans, insurance, or commerce, organize the test cases into domain-relevant groups and ensure coverage across those business areas.
- Generate ALL relevant test cases required to achieve adequate test coverage.
- Do not limit the number of test cases.
- Cover the following test design techniques whenever applicable:
  - Positive Testing
  - Negative Testing
  - Boundary Value Analysis
  - Equivalence Partitioning
  - Decision Table Testing
  - State Transition Testing
  - Error Guessing

- Include test types when applicable:
  - Functional
  - Validation
  - Boundary
  - Negative
  - Security
  - Performance
  - Usability
  - Integration
  - Data Validation

- Priorities must be:
  - High
  - Medium
  - Low

- Generate realistic and actionable test steps.
- Include database validations when database requirements are mentioned.
- Include API validations when API behavior is described.
- Include security validations when authentication, authorization, permissions, roles, tokens, sessions, passwords, or sensitive data are involved.
- Include performance validations when limits, concurrency, throughput, volume, scalability, or response times are mentioned.
- Include boundary validations for all numeric, length, date, quantity, and limit-based requirements.
- Include negative scenarios for invalid, missing, malformed, unauthorized, duplicated, and unexpected inputs.
- Each test case must validate only one primary objective.
- Expected results must be specific and verifiable.
- Avoid duplicate test cases.
- Be specific to the provided user story.
"""

    print("\n⏳ Generating test cases, please be patient...\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw = response.text.strip()

    # Remove markdown code blocks if Gemini adds them
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    data = json.loads(raw)

    test_cases = []
    for tc in data["test_cases"]:
        test_cases.append(
            TestCase(
                tc_id=tc["tc_id"],
                title=tc["title"],
                tc_type=tc["tc_type"],
                priority=tc["priority"],
                preconditions=tc.get("preconditions", ""),
                steps=tc.get("steps", []),
                expected_result=tc.get("expected_result", "")
            )
        )

    return test_cases