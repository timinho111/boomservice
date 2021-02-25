from django.urls import path, include


urlpatterns = [
    path('', include('boomservice.core.urls')),
]