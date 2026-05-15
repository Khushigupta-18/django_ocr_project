from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render


class BaseOCRView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    serializer_class = None
    extractor_function = None

    def get(self, request):
        return Response({"message": "Upload image using POST request"})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            image = serializer.validated_data["image"]

            result = self.__class__.extractor_function(image)
            return Response(result)

        return Response(serializer.errors)


# ✅ MOVE THIS OUTSIDE THE CLASS
def ocr_page(request):
    return render(request, "ocr/index.html")