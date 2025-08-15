import re

def extract_bill_details(text: str) -> dict:
    """
    Extract key details from OCR text: name, date, amount, hospital, diagnosis
    """
    name = re.search(r"Patient Name: (.+)", text)
    date = re.search(r"Date: (\d{2}/\d{2}/\d{4})", text)
    amount = re.search(r"Total Amount: \$?([\d,.]+)", text)
    hospital = re.search(r"Hospital: (.+)", text)
    diagnosis = re.search(r"Diagnosis: (.+)", text)

    return {
        "name": name.group(1) if name else None,
        "date": date.group(1) if date else None,
        "amount": amount.group(1) if amount else None,
        "hospital": hospital.group(1) if hospital else None,
        "diagnosis": diagnosis.group(1) if diagnosis else None
    }
