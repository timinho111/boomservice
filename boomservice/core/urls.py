from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view()),
    path('api/getPlayers/', views.get_players_from_api),
    path('api/players/', views.player_list)
]