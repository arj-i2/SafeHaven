from django import forms
from .models import (
    Resident,
    DisasterType,
    Incident,
    EvacuationCenter,
    RescueTeam,
    Response,
    Resource,
)

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = [
            'first_name',
            'last_name',
            'contact_number',
            'address',
            'birth_date',
        ]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class DisasterTypeForm(forms.ModelForm):
    class Meta:
        model = DisasterType
        fields = [
            'name',
            'description',
        ]


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'resident',
            'disaster_type',
            'title',
            'description',
            'address',
            'latitude',
            'longitude',
            'status',
        ]


class EvacuationCenterForm(forms.ModelForm):
    class Meta:
        model = EvacuationCenter
        fields = [
            'name',
            'address',
            'capacity',
            'current_occupants',
            'latitude',
            'longitude',
            'contact_person',
            'contact_number',
            'is_active',
        ]


class RescueTeamForm(forms.ModelForm):
    class Meta:
        model = RescueTeam
        fields = [
            'team_name',
            'team_leader',
            'contact_number',
            'members_count',
            'status',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'incident',
            'rescue_team',
            'status',
            'remarks',
        ]


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            'name',
            'category',
            'quantity',
            'unit',
            'description',
        ]
