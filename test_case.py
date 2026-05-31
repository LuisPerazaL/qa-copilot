class TestCase:
    def __init__(self, tc_id, title, tc_type, priority,
                 preconditions="", steps=None, expected_result=""):
        self.tc_id = tc_id
        self.title = title
        self.tc_type = tc_type
        self.priority = priority
        self.preconditions = preconditions
        self.steps = steps or []
        self.expected_result = expected_result

    def __str__(self):
        steps_str = "\n    ".join(
            f"{i+1}. {s}" for i, s in enumerate(self.steps)
        )
        return (
            f"\n{'='*55}\n"
            f"  {self.tc_id} | {self.title}\n"
            f"  Type: {self.tc_type} | Priority: {self.priority}\n"
            f"  Preconditions: {self.preconditions}\n"
            f"  Steps:\n    {steps_str}\n"
            f"  Expected Result: {self.expected_result}\n"
            f"{'='*55}"
        )