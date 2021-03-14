from rest_framework import serializers

from app.models import * 

class DriveLocUpdate(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['latitude','longitude']