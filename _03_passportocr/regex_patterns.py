import re

# Indian Passports: 1 Letter followed by 7 Digits
PASSPORT_REGEX = r"[A-Z][0-9]{7}"
DATE_REGEX = r"\d{2}/\d{2}/\d{4}"

def extract_passport_number(text):
    text = text.upper()
    match = re.search(PASSPORT_REGEX, text)
    return match.group() if match else None

def extract_dates(text):
    # Returns a list of all dates found (usually DOB and Expiry)
    dates = re.findall(DATE_REGEX, text)
    return dates

def extract_nationality(text):
    if "INDIAN" in text.upper() or "INDIA" in text.upper():
        return "INDIAN"
    return None

def extract_passport_name(text):
    """Extracts Name from the Machine Readable Zone (the <<<<< part)"""
    # Look for lines containing multiple '<'
    match = re.search(r"P<[A-Z]{3}([A-Z<]+)", text.upper())
    if match:
        name_part = match.group(1)
        # Replace << with space and clean up
        clean_name = name_part.replace("<<", " ").replace("<", " ").strip()
        return clean_name
    return None