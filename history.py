import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_to_history(requirement_id, user_story, test_cases):
    history = load_history()

    history[requirement_id] = {
        "requirement_id": requirement_id,
        "user_story": user_story,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "test_cases": [
            {
                "tc_id": tc.tc_id,
                "title": tc.title,
                "tc_type": tc.tc_type,
                "priority": tc.priority,
                "preconditions": tc.preconditions,
                "steps": tc.steps,
                "expected_result": tc.expected_result
            }
            for tc in test_cases
        ]
    }

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved to history as {requirement_id}.")


def list_history():
    history = load_history()

    if not history:
        print("\n⚠️  No history found.")
        return

    print("\n📋 Saved Requirements:\n")
    for i, (req_id, data) in enumerate(history.items(), 1):
        tc_count = len(data["test_cases"])
        generated_at = data["generated_at"]
        print(f"  {i}. {req_id} — {tc_count} test cases — {generated_at}")


def load_from_history(requirement_id):
    from test_case import TestCase

    history = load_history()

    if requirement_id not in history:
        return None

    data = history[requirement_id]
    test_cases = [
        TestCase(
            tc_id=tc["tc_id"],
            title=tc["title"],
            tc_type=tc["tc_type"],
            priority=tc["priority"],
            preconditions=tc.get("preconditions", ""),
            steps=tc.get("steps", []),
            expected_result=tc.get("expected_result", "")
        )
        for tc in data["test_cases"]
    ]

    return test_cases, data["user_story"]