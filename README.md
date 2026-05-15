# OCR Document API

A Django-based OCR API system for extracting text and details from multiple document types including:

- PAN Card
- Aadhar Card
- Passport

The project provides REST API endpoints for uploading document images and extracting OCR text data.

---

# Features

- PAN Card OCR API
- Aadhar Card OCR API
- Passport OCR API
- Universal OCR API
- Django REST Framework support
- JSON API responses
- Frontend OCR testing page
- Render deployment ready

---

# Tech Stack

- Python
- Django
- Django REST Framework
- OpenCV
- Pillow
- EasyOCR

---

# Screenshots

## Universal OCR
<img width="1304" height="576" alt="image" src="https://github.com/user-attachments/assets/6297859b-d94a-470f-b4a1-5e09e98fb936" />

---

## PAN Card OCR
<img width="939" height="444" alt="image" src="https://github.com/user-attachments/assets/1044aa49-2907-4999-abf1-5ab4d5426e36" />

---

## Aadhar Card OCR
<img width="900" height="518" alt="image" src="https://github.com/user-attachments/assets/f03c8045-66e5-40d7-a24e-c23d261cc998" />

---

## Passport OCR
<img width="923" height="571" alt="image" src="https://github.com/user-attachments/assets/4a190db6-98e2-4965-bdc8-28061e996929" />

---

# Project Structure

```bash
ocr/
│
├── manage.py
├── requirements.txt
├── Procfile
│
├── ocr/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── _01_panocr/
├── _02_aadharocr/
├── _03_passportocr/
├── _ocr_common/
```

---

# API Endpoints

## PAN Card OCR API

```http
POST /api/pan/upload/
```

---

## Aadhar Card OCR API

```http
POST /api/aadhar/upload/
```

---

## Passport OCR API

```http
POST /api/passport/upload/
```

---

## Universal OCR API

```http
POST /api/ocr/upload/
```

---

## Frontend OCR Page

```http
GET /ocr/
```

---

# Local Setup

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd ocr
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Development Server

bash
python manage.py runserver

Server will start at:
http://127.0.0.1:8000/

---

# Deployment
This project is deployment-ready for Render.

# License
This project is for educational and development purposes.

---

# Author
Khushi Gupta
