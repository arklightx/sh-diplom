from rest_framework import serializers

from .models import Requests


class RequestsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        Requests.objects.create(
            theme=validated_data["theme"],
            text=validated_data["text"],
            home=validated_data["home"],
            user=validated_data["user"]
        )
        return validated_data

    class Meta:
        model = Requests
        fields = "__all__"
