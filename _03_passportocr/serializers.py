from rest_framework import serializers
from _ocr_common.serializers import BaseOCRSerializer


class PassportOCRSerializer(BaseOCRSerializer):

    passport_number = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    date_of_birth = serializers.CharField(required=False)
    expiry_date = serializers.CharField(required=False)