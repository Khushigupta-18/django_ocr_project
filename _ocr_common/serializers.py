from rest_framework import serializers     #Python Object/Model → JSON(API Response), JSON(API Request) → Python Object
                                           #serializers - Converter between Python/Django data and JSON data used in APIs.

class BaseOCRSerializer(serializers.Serializer):

    image = serializers.ImageField()

    extracted_text = serializers.CharField(required=False)
    confidence_score = serializers.FloatField(required=False)