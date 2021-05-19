from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
from apps.works.models import Work, Secretary, WorkState, WorkCoordinate, WorkImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'is_staff']


class SecretarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretary
        fields = ['id', 'name', 'email', 'icon']


class WorkCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkCoordinate
        fields = ['id', 'name', 'work', 'latitude', 'longitude']


class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        fields = ['id', 'image', 'work']


class WorkStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkState
        fields = ['id', 'name']


# Serializers define the API representation.
class WorkSerializer(serializers.ModelSerializer):
    secretary = SecretarySerializer()
    actual_work_state = WorkStateSerializer()
    coordinates = WorkCoordinateSerializer(source='workcoordinate_set', many=True, read_only=True)
    gallery_images = WorkImageSerializer(source='workimage_set', many=True, read_only=True)

    class Meta:
        model = Work
        fields = [
            'id',
            'contract_id',
            'year',
            'contract_object',
            'total_value',
            'progress_work',
            'pqr',
            'secretary',
            'actual_work_state',
            'coordinates',
            'gallery_images',
        ]
