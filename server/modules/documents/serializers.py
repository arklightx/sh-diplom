from rest_framework import serializers as ser
from .models import Document, Disablings


class DocumentSerializer(ser.ModelSerializer):

    class Meta:
        model = Document
        fields = "__all__"

    
class DisablingsSerializer(ser.ModelSerializer):

    class Meta:
        model = Disablings
        fields = "__all__"