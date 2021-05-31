from django.urls import path, include

from rest_framework import routers

from apps.street_lighting.viewsets import *
from apps.street_lighting.views import *

router = routers.DefaultRouter()
#router.register('elements', ElementsViewSet, basename='Elements')
router.register('luminarias', LuminariaViewSet)
router.register('postes', PosteViewSet)
router.register('redes', RedViewSet)
router.register('camaras', CamaraViewSet)
router.register('transformadores', TransformadorViewSet)

urlpatterns = [
    path('api/v2/', include(router.urls)),
    path('api/v3/luminarias', LuminariaView),
]
