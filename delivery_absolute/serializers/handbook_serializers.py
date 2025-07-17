from delivery_absolute.models import PackageType, ServiceType, Status, TransportModel
from rest_framework import serializers


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name']

class TransportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportModel
        fields = ['id', 'name']

class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = ['id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']