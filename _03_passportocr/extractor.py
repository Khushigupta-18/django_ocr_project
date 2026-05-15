import pytesseract
import re
from _ocr_common.preprocess import preprocess_image

def clean_mrz_data(text, mode="numeric"):
    """Corrects common OCR character misidentifications."""
    corrections = {
        "numeric": {'O': '0', 'I': '1', 'L': '1', 'Z': '2', 'B': '8', 'S': '5', 'T': '7'},
        "alpha": {'0': 'O', '1': 'I', '5': 'S', '2': 'Z', '8': 'B'}
    }
    
    for char, replacement in corrections.get(mode, {}).items():
        text = text.replace(char, replacement)
    return text

def extract_passport_details(image):

    processed = preprocess_image(image)

    text = pytesseract.image_to_string(processed, config="--psm 6")

    passport_number = None
    name = None
    dob = None
    gender = None
    nationality = None
    expiry_date = None

    # Clean OCR text
    cleaned = text.replace(" ", "").replace("\n", "\n").upper()
    lines = cleaned.split("\n")

    # Keep only lines that look like MRZ
    mrz_lines = [line for line in lines if len(line) > 30 and "<" in line]

    if len(mrz_lines) >= 2:

        line1 = mrz_lines[0]
        line2 = mrz_lines[1]

        # Passport number
        passport_number = line2[0:9].replace("<", "")

        # Nationality
        nationality = line2[10:13]

        # DOB
        dob_raw = line2[13:19]
        dob = "19" + dob_raw[0:2] + "-" + dob_raw[2:4] + "-" + dob_raw[4:6]

        # Gender
        gender = line2[20]

        # Expiry date
        exp_raw = line2[21:27]
        expiry_date = "20" + exp_raw[0:2] + "-" + exp_raw[2:4] + "-" + exp_raw[4:6]

        # Name extraction
        name_parts = line1.split("<<")

        if len(name_parts) >= 2:
            surname = name_parts[0].replace("P<IND", "").replace("<", "")
            given = name_parts[1].replace("<", " ")
            name = (given + " " + surname).strip()

    return {
        "passport_number": passport_number,
        "name": name,
        "dob": dob,
        "gender": gender,
        "nationality": nationality,
        "expiry_date": expiry_date,
        "raw_text": text
    }