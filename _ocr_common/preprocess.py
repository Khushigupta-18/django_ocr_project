import cv2
import numpy as np

def preprocess_image(image):

    image.seek(0)
    file_bytes = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Invalid image uploaded")

    # Resize (important for OCR)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Bilateral filter (better than Gaussian for text)
    blur = cv2.bilateralFilter(gray, 9, 75, 75)

    # Otsu threshold (better for documents)
    _,    thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    
    # Morphological opening to remove noise
    kernel = np.ones((2,2), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Dilate to strengthen text
    processed = cv2.dilate(opening, kernel, iterations=1)

    return processed