from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()

router.register('residents', api_views.ResidentViewSet)
router.register('disaster-types', api_views.DisasterTypeViewSet)
router.register('incidents', api_views.IncidentViewSet)
router.register('evacuation-centers', api_views.EvacuationCenterViewSet)
router.register('rescue-teams', api_views.RescueTeamViewSet)
router.register('responses', api_views.ResponseViewSet)
router.register('resources', api_views.ResourceViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('residents/', views.resident_list, name='resident_list'),
    path('residents/add/', views.resident_create, name='resident_create'),
    path('residents/edit/<int:pk>/', views.resident_update, name='resident_update'),
    path('residents/delete/<int:pk>/', views.resident_delete, name='resident_delete'),

    path('disaster-types/', views.disaster_type_list, name='disaster_type_list'),
    path('disaster-types/add/', views.disaster_type_create, name='disaster_type_create'),
    path('disaster-types/edit/<int:pk>/', views.disaster_type_update, name='disaster_type_update'),
    path('disaster-types/delete/<int:pk>/', views.disaster_type_delete, name='disaster_type_delete'),

    path('incidents/', views.incident_list, name='incident_list'),
    path('incidents/add/', views.incident_create, name='incident_create'),
    path('incidents/edit/<int:pk>/', views.incident_update, name='incident_update'),
    path('incidents/delete/<int:pk>/', views.incident_delete, name='incident_delete'),

    path('evacuation-centers/', views.evacuation_center_list, name='evacuation_center_list'),
    path('evacuation-centers/add/', views.evacuation_center_create, name='evacuation_center_create'),
    path('evacuation-centers/edit/<int:pk>/', views.evacuation_center_update, name='evacuation_center_update'),
    path('evacuation-centers/delete/<int:pk>/', views.evacuation_center_delete, name='evacuation_center_delete'),

    path('rescue-teams/', views.rescue_team_list, name='rescue_team_list'),
    path('rescue-teams/add/', views.rescue_team_create, name='rescue_team_create'),
    path('rescue-teams/edit/<int:pk>/', views.rescue_team_update, name='rescue_team_update'),
    path('rescue-teams/delete/<int:pk>/', views.rescue_team_delete, name='rescue_team_delete'),

    path('responses/', views.response_list, name='response_list'),
    path('responses/add/', views.response_create, name='response_create'),
    path('responses/edit/<int:pk>/', views.response_update, name='response_update'),
    path('responses/delete/<int:pk>/', views.response_delete, name='response_delete'),

    path('resources/', views.resource_list, name='resource_list'),
    path('resources/add/', views.resource_create, name='resource_create'),
    path('resources/edit/<int:pk>/', views.resource_update, name='resource_update'),
    path('resources/delete/<int:pk>/', views.resource_delete, name='resource_delete'),

    path('api/', include(router.urls)),
    path('weather/', views.weather, name='weather'),
    path('map/', views.emergency_map, name='emergency_map'),
]
