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

class Pagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        })

class ElementsViewSet(viewsets.ViewSet):
    pagination_class = Pagination

    def list(self, request):
        elements = Elements(
            luminarias=Luminaria.objects.all(),
            postes=Poste.objects.all(),
            redes=Red.objects.all(),
            camaras=Camara.objects.all(),
            transformadores=Transformador.objects.all(),
        )
        serializer = ElementsSerializer(elements)
        return Response(serializer.data)
