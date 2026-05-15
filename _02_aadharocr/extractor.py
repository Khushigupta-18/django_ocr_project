from _ocr_common.ocr_engine import extract_text
from _ocr_common.utils import clean_text
from .regex_patterns import extract_aadhar, extract_dob, extract_gender
import re


def extract_aadhar_details(image_path):

    raw_text = extract_text(image_path)

    cleaned = clean_text(raw_text)

    aadhar_number = extract_aadhar(cleaned)
    dob = extract_dob(cleaned)
    gender = extract_gender(cleaned)

    name = None

    # 1️⃣ Try extracting name after "Name"
    name_match = re.search(r'Name[:\-]?\s*([A-Za-z ]+)', cleaned)
    re.IGNORECASE
    
    if name_match:
        name = name_match.group(1).strip()

    # Remove OCR garbage words
        name_parts = name.split()
        name = " ".join(name_parts[:2])
        
    return {
        "aadhar_number": aadhar_number,
        "name": name,
        "dob": dob,
        "gender": gender,
        "raw_text": cleaned
    }