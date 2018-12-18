from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Document

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class DocumentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Document
        fields = ('id', 'title', 'slug', 'doc_type', 'period', 'student')