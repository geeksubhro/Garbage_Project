from rest_framework import serializers
from . models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['employee', 'department']
        
class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'house_number','road','pin_code','road_namw','state_address','district_address']
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['employee', 'department']
