from .models import Lead
from .serializers import LeadSerializer, PlayerSerializer
from rest_framework import generics
from .services import get_players
from .models import Player
from rest_framework.response import Response
from rest_framework.decorators import api_view


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


def get_players_from_api(request):
    Player.objects.all().delete()
    players_request = get_players('163', '2020')
    players_list = players_request['response']
    for player in players_list:
        print(player)
        player_data = Player(
            name=player['player']['name'],
            firstName=player['player']['firstname'],
            lastName=player['player']['lastname'],
            age=player['player']['age'],
            nationality=player['player']['nationality'],
            height=player['player']['height'],
            weight=player['player']['weight'],
            injured=player['player']['injured'],
            photo=player['player']['photo'],
        )
        player_data.save()
        print('player: ' + player['player']['name'] + ' saved')


@api_view(['GET'])
def player_list(request):
    data = Player.objects.all()
    serializer = PlayerSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)
