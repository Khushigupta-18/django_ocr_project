from django.urls import path
from .views import PassportOCRView


urlpatterns = [
    path('upload/', PassportOCRView.as_view(), name='passport-ocr'),
]