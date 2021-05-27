from django.urls import path, include

from rest_framework import routers

from apps.street_lighting.viewsets import *

router = routers.DefaultRouter()
router.register('elements', ElementsViewSet, basename='Elements')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
