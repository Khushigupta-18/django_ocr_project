from rest_framework import serializers
from _ocr_common.serializers import BaseOCRSerializer


class AadharOCRSerializer(BaseOCRSerializer):

    aadhar_number = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    dob = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    address = serializers.CharField(required=False)