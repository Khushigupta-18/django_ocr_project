import re

PAN_REGEX = r"[A-Z]{5}[0-9O]{4}[A-Z]"
DOB_REGEX = r"\d{2}[/\-]\d{2}[/\-]\d{4}"

def extract_pan(text):
    # Ensure text is uppercase for matching
    text = text.upper()
    match = re.search(PAN_REGEX, text)
    if match:
        pan = match.group()
        # Clean potential OCR errors (O instead of 0) in the middle 4 digits
        prefix = pan[:5]
        middle = pan[5:9].replace('O', '0')
        suffix = pan[9:]
        return prefix + middle + suffix
    return None

def extract_dob(text):
    match = re.search(DOB_REGEX, text)
    return match.group().replace('-', '/') if match else None

def extract_name(text):
    """Simple logic: Name is usually the line after 'INCOME TAX DEPARTMENT'"""
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    for i, line in enumerate(lines):
        if "INCOME TAX" in line.upper():
            if i + 1 < len(lines):
                return lines[i+1]
    return None