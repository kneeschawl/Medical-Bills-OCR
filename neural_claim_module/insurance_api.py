import requests

MOCK_INSURANCE_API = "https://mock-insurance-api.com/submit_claim"

def submit_claim_to_insurance(bill_details: dict, fraud_flag: bool) -> dict:
    """
    Send bill details and fraud flag to insurance API
    """
    payload = {
        "name": bill_details.get('name'),
        "date": bill_details.get('date'),
        "amount": bill_details.get('amount'),
        "hospital": bill_details.get('hospital'),
        "diagnosis": bill_details.get('diagnosis'),
        "fraud_flag": fraud_flag
    }

    # For prototype, we mock response instead of real API
    response = {"status": "Submitted", "claim_id": "CLAIM12345"}
    
    # Uncomment for real API
    # r = requests.post(MOCK_INSURANCE_API, json=payload)
    # response = r.json()
    
    return response
