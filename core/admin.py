from django.contrib import admin
from .models import (
    Resident,
    DisasterType,
    Incident,
    EvacuationCenter,
    RescueTeam,
    Response,
    Resource,
)

admin.site.register(Resident)
admin.site.register(DisasterType)
admin.site.register(Incident)
admin.site.register(EvacuationCenter)
admin.site.register(RescueTeam)
admin.site.register(Response)
admin.site.register(Resource)
