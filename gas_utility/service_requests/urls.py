from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('resolve/<int:request_id>/', views.resolve_request, name='resolve_request'),
]
