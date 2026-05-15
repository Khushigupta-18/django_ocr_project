import pytesseract          #It allows Python programs to extract text from images using the Tesseract OCR engine.
import cv2
from .preprocess import preprocess_image

# Set tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):

    img = preprocess_image(image_path)

    # Better OCR configuration
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(
        img,
        lang='eng',
        config=config
    )

    return text