from rest_framework import serializers
from .models import Lead, Team


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'area', 'name', 'shortName', 'tla', 'crestUrl', 'address', 'phone', 'website', 'email', 'founded', 'clubColors', 'venue', 'squad')