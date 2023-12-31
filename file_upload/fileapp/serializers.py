from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField()
    processed = serializers.BooleanField()

    class Meta:
        model = File
        fields = ['file', 'uploaded_at', 'processed', ]


class FileCreateSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    processed = serializers.HiddenField(default=False)

    class Meta:
        model = File
        fields = ['file', 'processed', ]
