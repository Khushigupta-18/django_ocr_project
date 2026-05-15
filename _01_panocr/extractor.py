from _ocr_common.ocr_engine import extract_text
from .regex_patterns import extract_pan, extract_dob
import re


def extract_pan_details(image_path):

    raw_text = extract_text(image_path)

    lines = raw_text.split("\n")

    pan_number = None
    dob = None
    name = None
    father_name = None

    # Find PAN and DOB
    for line in lines:
        if not pan_number:
            pan_match = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", line)
            if pan_match:
                pan_number = pan_match.group()

        if not dob:
            dob_match = re.search(r"\d{2}/\d{2}/\d{4}", line)
            if dob_match:
                dob = dob_match.group()

    # Get index positions
    pan_index = None
    dob_index = None

    for i, line in enumerate(lines):

        if pan_number and pan_number in line:
            pan_index = i

        if dob and dob in line:
            dob_index = i

    # Extract possible name lines between PAN and DOB
    candidates = []

    if pan_index is not None and dob_index is not None:

        for line in lines[pan_index + 1:dob_index]:

            clean_line = re.sub(r'[^A-Za-z ]', '', line).strip()

            words = clean_line.split()

        # ignore headers like "Name", "Father's Name"
            if "NAME" in clean_line.upper():
                continue

            if 2 <= len(words) <= 3 and all(len(w) > 2 for w in words):
                candidates.append(clean_line)

    if candidates:
        name = candidates[0]

    if len(candidates) > 1:
        father_name = candidates[1]

    return {
        "pan_number": pan_number,
        "name": name,
        "father_name": father_name,
        "dob": dob,
        "extracted_text": raw_text,
        "confidence_score": 0.92
    }