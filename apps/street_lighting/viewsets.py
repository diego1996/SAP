import json

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins
from itertools import chain
from collections import namedtuple

# ViewSets define the view behavior.
from apps.street_lighting.models import *
from apps.street_lighting.serializers import *

Elements = namedtuple('Elements', ('luminarias', 'postes', 'redes', 'camaras', 'transformadores'))

class ElementsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = ElementsSerializer

    def get_queryset(self):
        result_list = list(chain(Luminaria.objects.all(), Poste.objects.all(), Red.objects.all(), Camara.objects.all(), Transformador.objects.all()))
        elements = Elements(
            luminarias=Luminaria.objects.all(),
            postes=Poste.objects.all(),
            redes=Red.objects.all(),
            camaras=Camara.objects.all(),
            transformadores=Transformador.objects.all(),
        )
        return elements
