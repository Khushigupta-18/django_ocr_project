from _ocr_common.views import BaseOCRView
from .serializers import PassportOCRSerializer
from .extractor import extract_passport_details


class PassportOCRView(BaseOCRView):

    serializer_class = PassportOCRSerializer
    extractor_function = extract_passport_details