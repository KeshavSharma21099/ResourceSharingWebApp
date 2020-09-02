from .models import Directory
from rest_framework import serializers


class DirectorySerializer(serializers.ModelSerializer):
    pages = serializers.StringRelatedField(many=True)
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Directory
        fields = ['name', 'subject', 'pages', 'children']
