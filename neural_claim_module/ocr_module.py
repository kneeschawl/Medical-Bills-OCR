import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    """
    OCR: Extract text from a medical bill image.
    """
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
