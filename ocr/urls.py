"""
URL configuration for ocr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import JsonResponse
from django.urls import path, include
from django.contrib import admin
from .views import universal_ocr
from _ocr_common.views import ocr_page


def home(request):
    return JsonResponse({
        "message": "OCR API Running",
        "endpoints": [
            "/api/ocr/upload/",
            "/api/pan/",
            "/api/aadhar/",
            "/api/passport/"
        ]
    })


urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),

    # Universal OCR
    path("api/ocr/upload/", universal_ocr, name="universal_ocr"),

    # Individual OCR APIs
    path('api/pan/', include('_01_panocr.urls')),
    path('api/aadhar/', include('_02_aadharocr.urls')),
    path('api/passport/', include('_03_passportocr.urls')),

    # Frontend page
    path("ocr/", ocr_page, name="ocr_page"),
]