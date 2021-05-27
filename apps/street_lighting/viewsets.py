import json

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins

# ViewSets define the view behavior.
from apps.street_lighting.models import *
from apps.street_lighting.serializers import *

class ElementsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Luminaria.objects.all()
    serializer_class = ElementsSerializer

    def get_queryset(self):
        return Luminaria.objects.all() | Poste.objects.all() | Red.objects.all() | Camara.objects.all() | Transformador.objects.all()