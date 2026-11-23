from rest_framework import viewsets

from .models import (
    Resident,
    DisasterType,
    Incident,
    EvacuationCenter,
    RescueTeam,
    Response,
    Resource,
)

from .serializers import (
    ResidentSerializer,
    DisasterTypeSerializer,
    IncidentSerializer,
    EvacuationCenterSerializer,
    RescueTeamSerializer,
    ResponseSerializer,
    ResourceSerializer,
)


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class DisasterTypeViewSet(viewsets.ModelViewSet):
    queryset = DisasterType.objects.all()
    serializer_class = DisasterTypeSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class EvacuationCenterViewSet(viewsets.ModelViewSet):
    queryset = EvacuationCenter.objects.all()
    serializer_class = EvacuationCenterSerializer


class RescueTeamViewSet(viewsets.ModelViewSet):
    queryset = RescueTeam.objects.all()
    serializer_class = RescueTeamSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
