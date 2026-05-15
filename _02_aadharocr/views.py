from _ocr_common.views import BaseOCRView
from .serializers import AadharOCRSerializer
from .extractor import extract_aadhar_details


class AadharOCRView(BaseOCRView):

    serializer_class = AadharOCRSerializer
    extractor_function = extract_aadhar_details