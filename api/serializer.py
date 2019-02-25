from rest_framework import serializers

from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Document
        fields = ('id', 'title', 'path', 'doc_type', 'period', 'student')
