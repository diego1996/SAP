from django.urls import path, include

from rest_framework import routers

from apps.works import views
from apps.works.viewsets import UserViewSet, WorkViewSet, SecretaryViewSet

router = routers.DefaultRouter()
router.register('users/all', UserViewSet)
router.register('secretaries/all', SecretaryViewSet)
router.register('works/all', WorkViewSet)

urlpatterns = [
    path('pqr/works/<int:work_id>/', views.pqr, name='pqr'),
    path('pqr/send-email/', views.send_email, name='send-email'),
    path('api/v1/', include(router.urls)),
]
