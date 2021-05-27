import json

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from collections import namedtuple

# ViewSets define the view behavior.
from apps.street_lighting.models import *
from apps.street_lighting.serializers import *

Elements = namedtuple('Elements', ('luminarias', 'postes', 'redes', 'camaras', 'transformadores'))

class ElementsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    def get_queryset(self):
        elements = Elements(
            luminarias=Luminaria.objects.all(),
            postes=Poste.objects.all(),
            redes=Red.objects.all(),
            camaras=Camara.objects.all(),
            transformadores=Transformador.objects.all(),
        )
        serializer = ElementsSerializer(elements)
        return Response(serializer.data)
