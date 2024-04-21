from rest_framework import serializers
from .models import SDSUESPORTS

class ESportsTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SDSUESPORTS
        fields = '__all__'