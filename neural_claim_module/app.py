import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from fastapi import FastAPI, UploadFile, File
from ocr_module import extract_text_from_image
from extractor import extract_bill_details
from fraud_checker import detect_fraud
from insurance_api import submit_claim_to_insurance

app = FastAPI(title="Neural Network & Insurance Claim Module")

claims_db = {}  # Simple in-memory DB

@app.post("/submit_bill/")
async def submit_bill(file: UploadFile = File(...)):
    """
    Accept bill image, extract details, run fraud detection, submit claim
    """
    # Save uploaded file
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb+") as f:
        f.write(file.file.read())
    
    # OCR
    text = extract_text_from_image(file_location)
    
    # Extract details
    details = extract_bill_details(text)
    
    # Fraud check
    fraud_flag = detect_fraud(details)
    
    # Submit to insurance
    claim_response = submit_claim_to_insurance(details, fraud_flag)
    
    # Store in DB
    claim_id = claim_response["claim_id"]
    claims_db[claim_id] = {
        "details": details,
        "fraud_flag": fraud_flag,
        "status": claim_response["status"]
    }
    
    return {"claim_id": claim_id, "status": claim_response["status"]}

@app.get("/claim_status/{claim_id}")
def claim_status(claim_id: str):
    """
    Check claim approval/rejection status
    """
    claim = claims_db.get(claim_id)
    if not claim:
        return {"error": "Claim not found"}
    return {"claim_id": claim_id, "status": claim["status"], "fraud_flag": claim["fraud_flag"], "details": claim["details"]}
