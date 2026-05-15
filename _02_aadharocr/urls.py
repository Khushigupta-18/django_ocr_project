from django.urls import path
from .views import AadharOCRView

urlpatterns = [
    path('upload/', AadharOCRView.as_view(), name="aadhar-ocr"),
]