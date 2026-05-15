def detect_document_type(text):
    text = text.upper()

    # PAN detection
    if "INCOME TAX DEPARTMENT" in text or "PERMANENT ACCOUNT NUMBER" in text:
        return "pan"

    # Aadhaar detection
    elif "GOVERNMENT OF INDIA" in text and "UIDAI" in text:
        return "aadhar"

    # Passport detection (MRZ lines)
    elif "P<" in text:
        return "passport"

    return "unknown"