from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import APIException

# Serializers define the API representation.
from apps.street_lighting.models import *

#Consultas
from django.db import connection

class ElementsSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    num_unico_rotulo = serializers.CharField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    latitude_desde = serializers.CharField()
    longitude_desde = serializers.CharField()
    latitude_hasta = serializers.CharField()
    longitude_hasta = serializers.CharField()
    direccion = serializers.CharField()
    ubicacion = serializers.CharField()
