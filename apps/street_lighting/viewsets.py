import json

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import namedtuple

# ViewSets define the view behavior.
from apps.street_lighting.models import *
from apps.street_lighting.serializers import *

#Consultas
from django.db import connection

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

class LuminariaViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Luminaria.objects.all()
    serializer_class = LuminariaSerializer

    def get_queryset(self):
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 20
            if latitude and longitude:
                cursor = connection.cursor()
                qry = 'SELECT * FROM (SELECT *, (((acos(sin(('+str(latitude)+'*pi()/180)) * sin((latitude*pi()/180))+cos(('+str(latitude)+'*pi()/180)) * cos((latitude*pi()/180)) * cos((('+str(longitude)+' - longitude)*pi()/180))))*180/pi())*60*1.1515*1609.344) as distance FROM street_lighting_luminaria)myTable WHERE distance <= '+str(distance)
                cursor.execute(qry)
                r = [dict((cursor.description[i][0], value) \
                   for i, value in enumerate(row)) for row in cursor.fetchall()]
                serializer = LuminariaSerializer(r)
                if serializer.is_valid():
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Luminaria.objects.all()
        except:
            raise Exception("Error in get request params")

'''class ElementsViewSet(viewsets.ViewSet):

    def list(self, request):
        elements = Elements(
            luminarias=Luminaria.objects.all(),
            postes=Poste.objects.all(),
            redes=Red.objects.all(),
            camaras=Camara.objects.all(),
            transformadores=Transformador.objects.all(),
        )
        serializer = ElementsSerializer(elements)
        return Response(serializer.data)'''
