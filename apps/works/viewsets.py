import json

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets

# ViewSets define the view behavior.
from apps.works.models import Work, Secretary
from apps.works.serializers import UserSerializer, WorkSerializer, SecretarySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SecretaryViewSet(viewsets.ModelViewSet):
    queryset = Secretary.objects.all()
    serializer_class = SecretarySerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def get_queryset(self):
        try:
            secretaries = self.request.query_params.get('secretaries', None)
            year = self.request.query_params.get('year', None)
            search = self.request.query_params.get('search', None)
            if search:
                return Work.objects.filter(
                    Q(contract_object__icontains=search) |
                    Q(year__icontains=search) |
                    Q(secretary__name__icontains=search) |
                    Q(actual_work_state__name__icontains=search) |
                    Q(pqr__icontains=search) |
                    Q(total_value__icontains=search) |
                    Q(contract_id__icontains=search)
                )
            if secretaries and year and secretaries != "[]":
                return Work.objects.filter(secretary_id__in=json.loads(secretaries), year=year)
            if secretaries and secretaries != "[]":
                return Work.objects.filter(secretary_id__in=json.loads(secretaries))
            if year:
                return Work.objects.filter(year=year)
            return Work.objects.all()
        except:
            raise Exception("Error in get request params")
