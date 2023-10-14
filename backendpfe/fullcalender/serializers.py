from rest_framework import serializers
from datetime import datetime
from .models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id','event')

