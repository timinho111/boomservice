from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from .services import get_players
from rest_framework.response import Response
from rest_framework.views import APIView


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class PlayersPage(APIView):
    def get(self,request):
        players_list = get_players('163', '2020')
        return Response(players_list)
