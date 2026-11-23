from rest_framework import serializers
from .models import (
    Resident,
    DisasterType,
    Incident,
    EvacuationCenter,
    RescueTeam,
    Response,
    Resource,
)


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'


class DisasterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterType
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'


class EvacuationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvacuationCenter
        fields = '__all__'


class RescueTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueTeam
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
