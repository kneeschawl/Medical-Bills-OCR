def detect_fraud(bill_details: dict) -> bool:
    """
    Simple fraud detection (can later replace with ML model)
    """
    try:
        amount = float(bill_details.get('amount', '0').replace(',', ''))
        if amount > 10000:  # Example threshold
            return True
    except:
        return True  # Treat extraction errors as suspicious
    return False
