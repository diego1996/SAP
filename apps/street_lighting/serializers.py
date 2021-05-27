from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import APIException

# Serializers define the API representation.
from apps.street_lighting.models import *

#Consultas
from django.db import connection

class LuminariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luminaria
        fields = '__all__'

class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'

class RedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Red
        fields = '__all__'

class CamaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camara
        fields = '__all__'

class TransformadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformador
        fields = '__all__'

class ElementsSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    luminarias = LuminariaSerializer(many=True)
    postes = PosteSerializer(many=True)
    redes = RedSerializer(many=True)
    camaras = CamaraSerializer(many=True)
    transformadores = TransformadorSerializer(many=True)
