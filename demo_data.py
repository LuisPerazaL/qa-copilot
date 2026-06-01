from test_case import TestCase

def get_demo_test_cases():

    return [

        TestCase(
            tc_id="TC001",
            title="Valid Login",
            tc_type="Functional",
            priority="High",
            preconditions="User account exists",
            steps=[
                "Navigate to login page",
                "Enter valid username",
                "Enter valid password",
                "Click Login"
            ],
            expected_result="User successfully logs in"
        ),

        TestCase(
            tc_id="TC002",
            title="Invalid Password",
            tc_type="Negative",
            priority="High",
            preconditions="User account exists",
            steps=[
                "Navigate to login page",
                "Enter valid username",
                "Enter invalid password",
                "Click Login"
            ],
            expected_result="Authentication error message is displayed"
        )

    ]
