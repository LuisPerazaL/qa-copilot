from test_case import TestCase

DOMAIN_KEYWORDS = {
    "Banking": ["banco", "banca", "cuenta", "transferencia", "tarjeta", "sucursal", "pago", "prestamo", "deposito", "retiro", "interes"],
    "Payments": ["pago", "transferencia", "cobro", "factura", "checkout", "monto", "tarjeta", "monedero", "saldo", "visa", "mastercard"],
    "Loans": ["prestamo", "credito", "interes", "cuota", "plazo", "amortizacion", "solicitud de prestamo"],
    "Security": ["seguridad", "autenticacion", "autorizacion", "token", "session", "contraseña", "password", "mfa", "otp", "bloqueo"],
    "Statements": ["estado de cuenta", "extracto", "movimientos", "historial", "facturacion", "reporte"],
    "Integration": ["api", "webhook", "integracion", "endpoint", "servicio externo"],
    "Performance": ["rendimiento", "carga", "concurrencia", "latencia", "velocidad", "tiempo de respuesta"],
    "Mobile": ["app", "movil", "aplicacion", "android", "ios", "pantalla pequeña"],
    "Insurance": ["seguro", "poliza", "prima", "asegurado", "cobertura"],
    "Ecommerce": ["ecommerce", "comercio", "tienda", "carrito", "checkout", "producto", "pedido", "venta", "carrito de compras"]
}

CATEGORIES = [
    {
        "domain": "Banking",
        "count": 24,
        "templates": [
            {
                "title": "Open new checking account",
                "tc_type": "Functional",
                "priority": "High",
                "preconditions": "Customer has valid identity documents",
                "steps": [
                    "Open account creation page",
                    "Enter customer name, contact, and identity details",
                    "Select checking account product",
                    "Submit the application"
                ],
                "expected_result": "New checking account is created and account number is displayed"
            },
            {
                "title": "Update account profile information",
                "tc_type": "Validation",
                "priority": "Medium",
                "preconditions": "Customer is authenticated",
                "steps": [
                    "Open profile settings",
                    "Edit address and contact details",
                    "Save changes"
                ],
                "expected_result": "Profile updates are accepted and displayed correctly"
            },
            {
                "title": "Close account with pending balance",
                "tc_type": "Boundary",
                "priority": "Medium",
                "preconditions": "Account balance is zero or positive",
                "steps": [
                    "Open account closure request",
                    "Verify pending fees and balance",
                    "Submit closure request"
                ],
                "expected_result": "Account closure succeeds only when balance is cleared"
            }
        ]
    },
    {
        "domain": "Payments",
        "count": 16,
        "templates": [
            {
                "title": "Send domestic transfer within limit",
                "tc_type": "Functional",
                "priority": "High",
                "preconditions": "Sender account has sufficient balance",
                "steps": [
                    "Open transfer form",
                    "Enter beneficiary account and amount",
                    "Confirm transfer"
                ],
                "expected_result": "Transfer is processed successfully and confirmation is shown"
            },
            {
                "title": "Send transfer exceeding daily limit",
                "tc_type": "Boundary",
                "priority": "High",
                "preconditions": "Sender has daily transfer limit",
                "steps": [
                    "Open transfer form",
                    "Enter amount greater than daily limit",
                    "Submit transfer"
                ],
                "expected_result": "System blocks transfer and displays limit error"
            },
            {
                "title": "Validate beneficiary account details",
                "tc_type": "Data Validation",
                "priority": "High",
                "preconditions": "Sending account is active",
                "steps": [
                    "Open beneficiary management",
                    "Enter beneficiary account number and routing details",
                    "Save beneficiary"
                ],
                "expected_result": "Beneficiary details are validated and saved only if valid"
            }
        ]
    },
    {
        "domain": "Loans",
        "count": 14,
        "templates": [
            {
                "title": "Submit loan application with valid income proof",
                "tc_type": "Functional",
                "priority": "High",
                "preconditions": "Customer is authenticated",
                "steps": [
                    "Open loan application form",
                    "Enter income, employment, and loan details",
                    "Upload proof documents",
                    "Submit application"
                ],
                "expected_result": "Loan application is accepted for review"
            },
            {
                "title": "Reject loan application with missing documents",
                "tc_type": "Negative",
                "priority": "High",
                "preconditions": "Customer has started a loan application",
                "steps": [
                    "Open loan application form",
                    "Leave required document fields empty",
                    "Submit application"
                ],
                "expected_result": "Application is rejected and error message identifies missing documents"
            },
            {
                "title": "Verify loan EMI calculation",
                "tc_type": "Boundary",
                "priority": "Medium",
                "preconditions": "Loan product and interest rate are selected",
                "steps": [
                    "Enter loan amount and tenure",
                    "Calculate EMI",
                    "Compare displayed EMI with expected formula"
                ],
                "expected_result": "EMI calculation is accurate for the given inputs"
            }
        ]
    },
    {
        "domain": "Security",
        "count": 14,
        "templates": [
            {
                "title": "Login with valid credentials",
                "tc_type": "Functional",
                "priority": "High",
                "preconditions": "User account exists",
                "steps": [
                    "Open login page",
                    "Enter valid username and password",
                    "Submit login"
                ],
                "expected_result": "User logs in successfully"
            },
            {
                "title": "Block account after repeated failed login attempts",
                "tc_type": "Negative",
                "priority": "High",
                "preconditions": "User account exists",
                "steps": [
                    "Attempt login with invalid password five times",
                    "Observe system behavior"
                ],
                "expected_result": "Account is temporarily blocked and security warning is shown"
            },
            {
                "title": "Validate multi-factor authentication workflow",
                "tc_type": "Security",
                "priority": "High",
                "preconditions": "User has MFA enabled",
                "steps": [
                    "Login with valid credentials",
                    "Enter OTP or approve push notification",
                    "Complete login"
                ],
                "expected_result": "MFA challenge is enforced and login completes only after successful verification"
            }
        ]
    },
    {
        "domain": "Statements",
        "count": 10,
        "templates": [
            {
                "title": "Download monthly account statement",
                "tc_type": "Functional",
                "priority": "Medium",
                "preconditions": "Account has transaction history",
                "steps": [
                    "Open statements section",
                    "Select monthly period",
                    "Download PDF"
                ],
                "expected_result": "Monthly statement downloads successfully and includes transactions"
            },
            {
                "title": "Filter transactions by date range",
                "tc_type": "Validation",
                "priority": "Medium",
                "preconditions": "Account history is available",
                "steps": [
                    "Open transaction history",
                    "Set valid start and end dates",
                    "Apply filter"
                ],
                "expected_result": "Displayed transactions match the selected date range"
            },
            {
                "title": "Export transaction history to CSV",
                "tc_type": "Usability",
                "priority": "Low",
                "preconditions": "Transaction list is populated",
                "steps": [
                    "Open export options",
                    "Select CSV format",
                    "Download file"
                ],
                "expected_result": "CSV file downloads and contains expected transaction fields"
            }
        ]
    },
    {
        "domain": "Integration",
        "count": 10,
        "templates": [
            {
                "title": "Call account balance API with valid token",
                "tc_type": "Integration",
                "priority": "High",
                "preconditions": "API token is valid",
                "steps": [
                    "Send balance request to API endpoint",
                    "Inspect response payload"
                ],
                "expected_result": "Response returns current balance with correct schema"
            },
            {
                "title": "Reject API request with invalid credentials",
                "tc_type": "Negative",
                "priority": "High",
                "preconditions": "API key is invalid",
                "steps": [
                    "Send authenticated API request with invalid token",
                    "Inspect response"
                ],
                "expected_result": "API returns unauthorized status and error message"
            },
            {
                "title": "Validate payment status webhook payload",
                "tc_type": "Data Validation",
                "priority": "Medium",
                "preconditions": "Webhook endpoint is configured",
                "steps": [
                    "Send simulated payment event to webhook",
                    "Verify received payload structure"
                ],
                "expected_result": "Webhook receives correct event data and acknowledges it"
            }
        ]
    },
    {
        "domain": "Performance",
        "count": 8,
        "templates": [
            {
                "title": "Load dashboard with many accounts",
                "tc_type": "Performance",
                "priority": "High",
                "preconditions": "User has access to multiple accounts",
                "steps": [
                    "Open dashboard page",
                    "Measure time to load account summary"
                ],
                "expected_result": "Dashboard loads within acceptable performance threshold"
            },
            {
                "title": "Process batch salary payments",
                "tc_type": "Performance",
                "priority": "High",
                "preconditions": "Batch file contains 1000 transactions",
                "steps": [
                    "Upload salary batch file",
                    "Start processing",
                    "Monitor completion time"
                ],
                "expected_result": "Batch is processed successfully within performance limits"
            },
            {
                "title": "Enforce maximum file upload size",
                "tc_type": "Boundary",
                "priority": "Medium",
                "preconditions": "Document upload is required",
                "steps": [
                    "Upload file larger than allowed size",
                    "Submit"
                ],
                "expected_result": "System rejects the file and shows appropriate size limit message"
            }
        ]
    },
    {
        "domain": "Mobile",
        "count": 8,
        "templates": [
            {
                "title": "Complete payment flow on mobile",
                "tc_type": "Usability",
                "priority": "Medium",
                "preconditions": "Mobile app is installed",
                "steps": [
                    "Open mobile app",
                    "Navigate to payments",
                    "Make a fund transfer"
                ],
                "expected_result": "Payment flow completes successfully on mobile"
            },
            {
                "title": "Verify responsive layout on a small screen",
                "tc_type": "Usability",
                "priority": "Low",
                "preconditions": "Mobile device screen is narrow",
                "steps": [
                    "Open app on mobile device",
                    "Review key screens for layout issues"
                ],
                "expected_result": "UI elements adapt with no overlap or truncation"
            },
            {
                "title": "Check accessibility labels on mobile",
                "tc_type": "Usability",
                "priority": "Low",
                "preconditions": "Accessibility mode is enabled",
                "steps": [
                    "Enable screen reader",
                    "Navigate through the app"
                ],
                "expected_result": "All interactive elements have accessible labels"
            }
        ]
    },
    {
        "domain": "Insurance",
        "count": 9,
        "templates": [
            {
                "title": "Submit insurance premium payment",
                "tc_type": "Functional",
                "priority": "Medium",
                "preconditions": "Insurance policy is active",
                "steps": [
                    "Open insurance payment section",
                    "Enter premium amount and payment method",
                    "Confirm payment"
                ],
                "expected_result": "Premium payment is accepted and receipt is generated"
            },
            {
                "title": "View insurance invoice details",
                "tc_type": "Functional",
                "priority": "Medium",
                "preconditions": "User has an active policy",
                "steps": [
                    "Open policy invoices",
                    "Select current billing cycle"
                ],
                "expected_result": "Invoice details display correct premium and due date"
            },
            {
                "title": "Reject expired card payment",
                "tc_type": "Negative",
                "priority": "High",
                "preconditions": "Payment card on file is expired",
                "steps": [
                    "Attempt to pay premium with expired card",
                    "Submit payment"
                ],
                "expected_result": "Payment is declined and an expired card error is shown"
            }
        ]
    },
    {
        "domain": "Ecommerce",
        "count": 24,
        "templates": [
            {
                "title": "Add product to shopping cart",
                "tc_type": "Functional",
                "priority": "High",
                "preconditions": "Product is in stock",
                "steps": [
                    "Open the product page",
                    "Select quantity",
                    "Add product to the cart"
                ],
                "expected_result": "Product is added to the cart and cart count updates"
            },
            {
                "title": "Complete checkout with valid payment",
                "tc_type": "Functional",
                "priority": "High",
                "preconditions": "Shopping cart contains at least one product",
                "steps": [
                    "Go to checkout page",
                    "Enter shipping address and payment details",
                    "Submit order"
                ],
                "expected_result": "Order completes successfully and confirmation is displayed"
            },
            {
                "title": "Validate coupon code discount",
                "tc_type": "Data Validation",
                "priority": "Medium",
                "preconditions": "Coupon code is valid",
                "steps": [
                    "Open checkout page",
                    "Enter coupon code",
                    "Apply discount"
                ],
                "expected_result": "Discount is applied correctly to the order total"
            }
        ]
    }
]


def infer_domains(user_story):
    story = (user_story or "").lower()
    matched_domains = []
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(keyword in story for keyword in keywords):
            matched_domains.append(domain)
    return matched_domains


def get_demo_test_cases(user_story=None):
    selected_domains = infer_domains(user_story)
    if not selected_domains:
        selected_categories = CATEGORIES
    else:
        selected_categories = [cat for cat in CATEGORIES if cat["domain"] in selected_domains]
        if not selected_categories:
            selected_categories = CATEGORIES

    total_target = 100
    per_category = max(20, total_target // len(selected_categories))

    test_cases = []
    sequence = 1

    for category in selected_categories:
        count = max(category["count"], per_category)
        templates = category["templates"]
        for idx in range(count):
            template = templates[idx % len(templates)]
            repeat = idx // len(templates) + 1
            title_suffix = f" - Scenario {repeat}" if repeat > 1 else ""
            title = f"{category['domain']}: {template['title']}{title_suffix}"
            test_cases.append(
                TestCase(
                    tc_id=f"TC{sequence:03d}",
                    title=title,
                    tc_type=template["tc_type"],
                    priority=template["priority"],
                    preconditions=f"Domain: {category['domain']}. {template['preconditions']}",
                    steps=template["steps"],
                    expected_result=template["expected_result"]
                )
            )
            sequence += 1

    return test_cases
