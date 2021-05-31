import json

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.http import JsonResponse
from collections import namedtuple

# ViewSets define the view behavior.
from rest_framework import status
from rest_framework.decorators import api_view
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

@api_view(['GET'])
def LuminariaView(request):
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)
    distance = 20
    try:
        if latitude and longitude:
            cursor = connection.cursor()
            #qry = 'SELECT * FROM street_lighting_luminaria LIMIT 1'
            query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_luminaria GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC"
            cursor.execute(query)
            r = [dict((cursor.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cursor.fetchall()]
            if r:
                return Response(r, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        raise Exception("Error in get request params")






'''class LuminariaViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Luminaria.objects.all()
    serializer_class = LuminariaSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        distance = 20
        cursor = connection.cursor()
        qry = 'SELECT * FROM (SELECT *, (((acos(sin(('+str(latitude)+'*pi()/180)) * sin((latitude*pi()/180))+cos(('+str(latitude)+'*pi()/180)) * cos((latitude*pi()/180)) * cos((('+str(longitude)+' - longitude)*pi()/180))))*180/pi())*60*1.1515*1609.344) as distance FROM street_lighting_luminaria)myTable WHERE distance <= '+str(distance)+' LIMIT 1'
        cursor.execute(qry)
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 20
            if latitude and longitude:
                cursor = connection.cursor()
                print(latitude)
                qry = 'SELECT * FROM (SELECT *, (((acos(sin(('+str(latitude)+'*pi()/180)) * sin((latitude*pi()/180))+cos(('+str(latitude)+'*pi()/180)) * cos((latitude*pi()/180)) * cos((('+str(longitude)+' - longitude)*pi()/180))))*180/pi())*60*1.1515*1609.344) as distance FROM street_lighting_luminaria)myTable WHERE distance <= '+str(distance)+' LIMIT 1'
                cursor.execute(qry)
                r = [dict((cursor.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cursor.fetchall()]

                if r:
                    raise serializers.ValidationError(r)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Luminaria.objects.all()
        except:
            raise Exception("Error in get request params")

class ElementsViewSet(viewsets.ViewSet):

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
