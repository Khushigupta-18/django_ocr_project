from django.urls import path
from .views import PanOCRView

urlpatterns = [
    path("upload/", PanOCRView.as_view(), name="pan-ocr"),
]