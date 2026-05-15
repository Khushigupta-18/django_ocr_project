from django.http import JsonResponse
import pytesseract

from _ocr_common.preprocess import preprocess_image
from _ocr_common.detect import detect_document_type
from django.views.decorators.csrf import csrf_exempt


from _01_panocr.extractor import extract_pan_details
from _02_aadharocr.extractor import extract_aadhar_details
from _03_passportocr.extractor import extract_passport_details

@csrf_exempt
def universal_ocr(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required"})

    image = request.FILES.get("image")

    if not image:
        return JsonResponse({"error": "No image uploaded"})

    # Preprocess
    processed = preprocess_image(image)

    # OCR text (run once)
    text = pytesseract.image_to_string(processed)

    # Detect document type
    doc_type = detect_document_type(text)

    # Route to correct extractor
    if doc_type == "pan":
        data = extract_pan_details(image)

    elif doc_type == "aadhar":
        data = extract_aadhar_details(image)

    elif doc_type == "passport":
        data = extract_passport_details(image)

    else:
        return JsonResponse({
            "error": "Document not recognized",
            "raw_text": text
        })

    # Add detected type
    data["document_type"] = doc_type

    return JsonResponse(data)