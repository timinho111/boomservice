from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
import requests


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class MyOwnView(generics.GenericAPIView):
    def get(self, request):
        result = {}
        url = requests.get('https://v3.football.api-sports.io/players?team=163')
        headers = {'x-rapidapi-host': "v3.football.api-sports.io", 'x-rapidapi-key': "e6de83259e8d932f70b56603587dcd99"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found'
            else:
                result['message'] = 'Football data not available'
        return response.json()
