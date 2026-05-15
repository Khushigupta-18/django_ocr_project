import re

# Matches 12 digits with optional spaces/dashes
AADHAR_REGEX = r"\b\d{4}\s?\d{4}\s?\d{4}\b"
# Matches DD/MM/YYYY or just YYYY
DOB_REGEX = r"(\d{2}/\d{2}/\d{4}|\d{4})"

def extract_aadhar(text):
    match = re.search(AADHAR_REGEX, text)
    if match:
        # Remove spaces to return a clean 12-digit string
        return match.group().replace(" ", "").replace("-", "")
    return None

def extract_dob(text):
    match = re.search(DOB_REGEX, text)
    return match.group() if match else None

def extract_gender(text):
    upper_text = text.upper()
    if "FEMALE" in upper_text:
        return "Female"
    if "MALE" in upper_text:
        return "Male"
    return None