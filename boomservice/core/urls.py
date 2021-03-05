from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view()),
    path('api/hello/', views.PlayersPage.as_view(), name='team'),
]