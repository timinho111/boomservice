from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from django.http import JsonResponse


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


def hello(request):
    return JsonResponse({'response_text':'hello world!'})