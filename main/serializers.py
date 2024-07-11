from rest_framework import serializers
from .models import LastestUpdates

class LatestUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastestUpdates
        fields = '__all__'