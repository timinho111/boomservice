from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view()),
    path('api/hello/', views.hello, name='hello'),
]