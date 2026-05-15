from rest_framework import serializers

class PanOCRSerializer(serializers.Serializer):

    image = serializers.ImageField(write_only=True)

    extracted_text = serializers.CharField(read_only=True)
    confidence_score = serializers.FloatField(read_only=True)

    pan_number = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    father_name = serializers.CharField(read_only=True)
    dob = serializers.CharField(read_only=True)