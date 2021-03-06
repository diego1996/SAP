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
            query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_luminaria GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC LIMIT 0,20"
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


class LuminariaViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Luminaria.objects.all()
    serializer_class = LuminariaSerializer
    pagination_class = Pagination

    def get_queryset(self):
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 50
            if latitude and longitude:
                cursor = connection.cursor()
                query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_luminaria GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC LIMIT 0,20"
                cursor.execute(query)
                ids = [row[0] for row in cursor.fetchall()]
                return Luminaria.objects.filter(id__in=ids)
            return Luminaria.objects.all()
        except:
            raise Exception("Error in get request params")

class PosteViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer
    pagination_class = Pagination

    def get_queryset(self):
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 50
            if latitude and longitude:
                cursor = connection.cursor()
                query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_poste GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC LIMIT 0,20"
                cursor.execute(query)
                ids = [row[0] for row in cursor.fetchall()]
                return Poste.objects.filter(id__in=ids)
            return Poste.objects.all()
        except:
            raise Exception("Error in get request params")

class RedViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Red.objects.all()
    serializer_class = RedSerializer
    pagination_class = Pagination

    def get_queryset(self):
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 50
            if latitude and longitude:
                cursor = connection.cursor()
                query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_red GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC LIMIT 0,20"
                cursor.execute(query)
                ids = [row[0] for row in cursor.fetchall()]
                return Red.objects.filter(id__in=ids)
            return Red.objects.all()
        except:
            raise Exception("Error in get request params")

class CamaraViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Camara.objects.all()
    serializer_class = CamaraSerializer
    pagination_class = Pagination

    def get_queryset(self):
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 50
            if latitude and longitude:
                cursor = connection.cursor()
                query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_camara GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC LIMIT 0,20"
                cursor.execute(query)
                ids = [row[0] for row in cursor.fetchall()]
                return Camara.objects.filter(id__in=ids)
            return Camara.objects.all()
        except:
            raise Exception("Error in get request params")

class TransformadorViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Transformador.objects.all()
    serializer_class = TransformadorSerializer
    pagination_class = Pagination

    def get_queryset(self):
        try:
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            distance = 50
            if latitude and longitude:
                cursor = connection.cursor()
                query = "SELECT id, ((ACOS(SIN("+latitude+" * PI() / 180) * SIN(latitude * PI() / 180) + COS("+latitude+" * PI() / 180) * COS(latitude * PI() / 180) * COS(("+longitude+" - longitude) * PI() / 180)) * 180 / PI()) * 60 * 1.1515 * 1609.344) AS distance FROM street_lighting_transformador GROUP BY id HAVING distance<='"+str(distance)+"' ORDER BY distance ASC LIMIT 0,20"
                cursor.execute(query)
                ids = [row[0] for row in cursor.fetchall()]
                return Transformador.objects.filter(id__in=ids)
            return Transformador.objects.all()
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
