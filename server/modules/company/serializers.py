from rest_framework import serializers
from .models import Company, CompanyServices


class CompanyServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyServices
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    services = CompanyServicesSerializer(many = True, read_only = True)
    class Meta:
        model = Company
        fields = "__all__"
