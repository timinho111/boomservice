from rest_framework import serializers
from .models import Lead, Player, Team


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'firstName', 'lastName', 'age', 'nationality', 'height', 'weight', 'injured', 'photo')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'area', 'name', 'shortName', 'tla', 'crestUrl', 'address', 'phone', 'website', 'email', 'founded', 'clubColors', 'venue', 'squad')