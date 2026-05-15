from _ocr_common.views import BaseOCRView
from .serializers import PanOCRSerializer
from .extractor import extract_pan_details


class PanOCRView(BaseOCRView):

    serializer_class = PanOCRSerializer
    extractor_function = extract_pan_details