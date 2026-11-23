from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Resident,
    DisasterType,
    Incident,
    EvacuationCenter,
    RescueTeam,
    Response,
    Resource,
)
from .forms import (
    ResidentForm,
    DisasterTypeForm,
    IncidentForm,
    EvacuationCenterForm,
    RescueTeamForm,
    ResponseForm,
    ResourceForm,
)
import json
from datetime import datetime, timedelta, timezone as dt_timezone
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError
from django.conf import settings


def home(request):
    return render(request, 'core/home.html')


def dashboard(request):
    context = {
        'resident_count': Resident.objects.count(),
        'disaster_type_count': DisasterType.objects.count(),
        'incident_count': Incident.objects.count(),
        'center_count': EvacuationCenter.objects.count(),
        'team_count': RescueTeam.objects.count(),
        'response_count': Response.objects.count(),
        'resource_count': Resource.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)


def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'core/resident_list.html', {
        'residents': residents
    })


def resident_create(request):
    form = ResidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resident_list')
    return render(request, 'core/resident_form.html', {'form': form})


def resident_update(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    form = ResidentForm(request.POST or None, instance=resident)
    if form.is_valid():
        form.save()
        return redirect('resident_list')
    return render(request, 'core/resident_form.html', {'form': form})


def resident_delete(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == 'POST':
        resident.delete()
        return redirect('resident_list')
    return render(request, 'core/resident_confirm_delete.html', {
        'resident': resident
    })


def disaster_type_list(request):
    disaster_types = DisasterType.objects.all()
    return render(request, 'core/disaster_type_list.html', {
        'disaster_types': disaster_types
    })


def disaster_type_create(request):
    form = DisasterTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('disaster_type_list')
    return render(request, 'core/disaster_type_form.html', {
        'form': form
    })


def disaster_type_update(request, pk):
    disaster_type = get_object_or_404(DisasterType, pk=pk)
    form = DisasterTypeForm(request.POST or None, instance=disaster_type)
    if form.is_valid():
        form.save()
        return redirect('disaster_type_list')
    return render(request, 'core/disaster_type_form.html', {
        'form': form
    })


def disaster_type_delete(request, pk):
    disaster_type = get_object_or_404(DisasterType, pk=pk)
    if request.method == 'POST':
        disaster_type.delete()
        return redirect('disaster_type_list')
    return render(request, 'core/disaster_type_confirm_delete.html', {
        'disaster_type': disaster_type
    })


def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'core/incident_list.html', {
        'incidents': incidents
    })


def incident_create(request):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('incident_list')
    return render(request, 'core/incident_form.html', {'form': form})


def incident_update(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    form = IncidentForm(request.POST or None, instance=incident)
    if form.is_valid():
        form.save()
        return redirect('incident_list')
    return render(request, 'core/incident_form.html', {'form': form})


def incident_delete(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        incident.delete()
        return redirect('incident_list')
    return render(request, 'core/incident_confirm_delete.html', {
        'incident': incident
    })


def evacuation_center_list(request):
    centers = EvacuationCenter.objects.all()
    return render(request, 'core/evacuation_center_list.html', {
        'centers': centers
    })


def evacuation_center_create(request):
    form = EvacuationCenterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('evacuation_center_list')
    return render(request, 'core/evacuation_center_form.html', {
        'form': form
    })


def evacuation_center_update(request, pk):
    center = get_object_or_404(EvacuationCenter, pk=pk)
    form = EvacuationCenterForm(request.POST or None, instance=center)
    if form.is_valid():
        form.save()
        return redirect('evacuation_center_list')
    return render(request, 'core/evacuation_center_form.html', {
        'form': form
    })


def evacuation_center_delete(request, pk):
    center = get_object_or_404(EvacuationCenter, pk=pk)
    if request.method == 'POST':
        center.delete()
        return redirect('evacuation_center_list')
    return render(request, 'core/evacuation_center_confirm_delete.html', {
        'center': center
    })




def rescue_team_list(request):
    teams = RescueTeam.objects.all()
    return render(request, 'core/rescue_team_list.html', {
        'teams': teams
    })


def rescue_team_create(request):
    form = RescueTeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rescue_team_list')
    return render(request, 'core/rescue_team_form.html', {
        'form': form
    })


def rescue_team_update(request, pk):
    team = get_object_or_404(RescueTeam, pk=pk)
    form = RescueTeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('rescue_team_list')
    return render(request, 'core/rescue_team_form.html', {
        'form': form
    })


def rescue_team_delete(request, pk):
    team = get_object_or_404(RescueTeam, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('rescue_team_list')
    return render(request, 'core/rescue_team_confirm_delete.html', {
        'team': team
    })



def response_list(request):
    responses = Response.objects.select_related(
        'incident', 'rescue_team'
    ).all()
    return render(request, 'core/response_list.html', {
        'responses': responses
    })


def response_create(request):
    form = ResponseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('response_list')
    return render(request, 'core/response_form.html', {
        'form': form
    })


def response_update(request, pk):
    response = get_object_or_404(Response, pk=pk)
    form = ResponseForm(request.POST or None, instance=response)
    if form.is_valid():
        form.save()
        return redirect('response_list')
    return render(request, 'core/response_form.html', {
        'form': form
    })


def response_delete(request, pk):
    response = get_object_or_404(Response, pk=pk)
    if request.method == 'POST':
        response.delete()
        return redirect('response_list')
    return render(request, 'core/response_confirm_delete.html', {
        'response': response
    })


def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'core/resource_list.html', {
        'resources': resources
    })


def resource_create(request):
    form = ResourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resource_list')
    return render(request, 'core/resource_form.html', {
        'form': form
    })


def resource_update(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    form = ResourceForm(request.POST or None, instance=resource)
    if form.is_valid():
        form.save()
        return redirect('resource_list')
    return render(request, 'core/resource_form.html', {
        'form': form
    })


def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    return render(request, 'core/resource_confirm_delete.html', {
        'resource': resource
    })




def weather(request):
    city = request.GET.get('city', '').strip()

    weather_data = None
    error_message = None
    message = None

    if not city:
        message = 'Please enter a city to view its weather.'

        return render(request, 'core/weather.html', {
            'weather_data': None,
            'error_message': None,
            'search_city': '',
            'message': message,
        })

    api_key = settings.OPENWEATHER_API_KEY

    if not api_key:
        error_message = (
            'OpenWeatherMap API key is missing. '
            'Please check your .env configuration.'
        )

        return render(request, 'core/weather.html', {
            'weather_data': None,
            'error_message': error_message,
            'search_city': city,
        })

    try:
        weather_url = (
            'https://api.openweathermap.org/data/2.5/weather?'
            + urlencode({
                'q': city,
                'appid': api_key,
                'units': 'metric',
            })
        )

        with urlopen(weather_url, timeout=15) as response:
            api_data = json.loads(response.read().decode('utf-8'))

        current = api_data['main']
        weather_condition = api_data['weather'][0]
        wind = api_data.get('wind', {})

        timezone_offset = api_data.get('timezone', 0)

        local_time = (
            datetime.fromtimestamp(api_data['dt'], dt_timezone.utc)
            + timedelta(seconds=timezone_offset)
        )

        sunrise = (
            datetime.fromtimestamp(
                api_data['sys']['sunrise'], dt_timezone.utc
            )
            + timedelta(seconds=timezone_offset)
        )

        sunset = (
            datetime.fromtimestamp(
                api_data['sys']['sunset'], dt_timezone.utc
            )
            + timedelta(seconds=timezone_offset)
        )

        weather_data = {
            'city': api_data['name'],
            'country': api_data['sys']['country'],
            'current': {
                'temperature': current['temp'],
                'feels_like': current['feels_like'],
                'humidity': current['humidity'],
                'wind_speed': round(wind.get('speed', 0) * 3.6, 1),
                'precipitation': api_data.get('rain', {}).get('1h', 0),
                'description': weather_condition['description'].title(),
                'icon': weather_condition['icon'],
                'is_day': sunrise <= local_time < sunset,
                'time': local_time.strftime('%B %d, %Y %I:%M %p'),
            }
        }

    except HTTPError as error:
        if error.code == 401:
            error_message = (
                'Invalid or inactive OpenWeatherMap API key. '
                'Check your API key and account activation.'
            )
        elif error.code == 404:
            error_message = (
                'City not found. Please check the spelling and try again.'
            )
        elif error.code == 429:
            error_message = (
                'API request limit reached. Please try again later.'
            )
        else:
            error_message = (
                f'OpenWeatherMap returned an error (HTTP {error.code}).'
            )

    except (URLError, TimeoutError):
        error_message = (
            'Unable to connect to OpenWeatherMap. '
            'Please check your internet connection.'
        )

    except (ValueError, KeyError, TypeError, IndexError):
        error_message = (
            'Unable to process the weather information. '
            'Please try again later.'
        )

    return render(request, 'core/weather.html', {
        'weather_data': weather_data,
        'error_message': error_message,
        'search_city': city,
        'message': message,
    })


def emergency_map(request):
    incidents = Incident.objects.exclude(
        latitude__isnull=True
    ).exclude(
        longitude__isnull=True
    ).values(
        'title',
        'address',
        'latitude',
        'longitude',
        'status'
    )

    centers = EvacuationCenter.objects.exclude(
        latitude__isnull=True
    ).exclude(
        longitude__isnull=True
    ).values(
        'name',
        'address',
        'latitude',
        'longitude',
        'is_active'
    )

    return render(request, 'core/map.html', {
        'incidents': list(incidents),
        'centers': list(centers),
        'maptiler_api_key': settings.MAPTILER_API_KEY,
    })