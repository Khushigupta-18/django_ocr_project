import re


def extract_pan_number(text):

    match = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", text)

    if match:
        return match.group()

    return None


def extract_aadhaar_number(text):

    match = re.search(r"\d{4}\s\d{4}\s\d{4}", text)

    if match:
        return match.group()

    return None


def extract_passport_number(text):

    # Common passport format (India & many countries)
    match = re.search(r"[A-Z][0-9]{7}", text)

    if match:
        return match.group()

    return None


def extract_passport_dates(text):

    # Matches dates like 01/01/1995 or 01-01-1995
    dates = re.findall(r"\d{2}[/-]\d{2}[/-]\d{4}", text)
    dob = dates[0] if len(dates) > 0 else None
    expiry = dates[1] if len(dates) > 1 else None

    return dob, expiry