from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *


# Register your models here.

class LuminariaResource(resources.ModelResource):
    class Meta:
        model = Luminaria


class PosteResource(resources.ModelResource):
    class Meta:
        model = Poste


class RedResource(resources.ModelResource):
    class Meta:
        model = Red


class CamaraResource(resources.ModelResource):
    class Meta:
        model = Camara


class TransformadorResource(resources.ModelResource):
    class Meta:
        model = Transformador


@admin.register(Luminaria)
class LuminariaAdmin(ImportExportModelAdmin):
    resource_class = LuminariaResource
    list_display = (
        'num_unico_rotulo', 'latitude', 'longitude', 'ubicacion', 'tipo_fuente_luminica', 'potencia', 'tipo_luminaria',
        'tipo_balastro', 'control_encendido', 'identificacion_transformador', 'nivel_tension'
    )
    search_fields = list_display
    list_filter = ('tipo_fuente_luminica', 'tipo_balastro')


@admin.register(Poste)
class PosteAdmin(ImportExportModelAdmin):
    resource_class = PosteResource
    list_display = (
        'num_unico_rotulo', 'latitude', 'longitude', 'ubicacion', 'exclusivo_compartido', 'tipo_material', 'longitud',
        'costo_unidad_constructiva'
    )
    search_fields = list_display
    list_filter = ('exclusivo_compartido', 'tipo_material')


@admin.register(Red)
class RedAdmin(ImportExportModelAdmin):
    resource_class = RedResource
    list_display = (
        'num_unico_rotulo', 'latitude_desde', 'longitude_desde', 'latitude_hasta', 'longitude_hasta', 'direccion',
        'exclusivo_compartido', 'tipo_material', 'calibre_conductores', 'tipo_instalacion', 'costo_unidad_constructiva'
    )
    search_fields = list_display
    list_filter = (
        'exclusivo_compartido', 'tipo_material', 'tipo_instalacion',
    )


@admin.register(Camara)
class CamaraAdmin(ImportExportModelAdmin):
    resource_class = CamaraResource
    list_display = (
        'num_unico_rotulo', 'latitude_desde', 'longitude_desde', 'latitude_hasta', 'longitude_hasta', 'direccion',
        'exclusivo_compartido', 'cajas_inspeccion', 'ducterias', 'tipo_zona', 'costo_unidad_constructiva'
    )
    search_fields = list_display
    list_filter = (
        'exclusivo_compartido', 'cajas_inspeccion', 'tipo_zona',
    )


@admin.register(Transformador)
class TransformadorAdmin(ImportExportModelAdmin):
    resource_class = TransformadorResource
    list_display = (
        'num_unico_rotulo', 'latitude', 'longitude', 'ubicacion', 'exclusivo_compartido', 'tipo', 'capacidad',
        'valor_catastral', 'area_terreno', 'costo_unidad_constructiva'
    )
    search_fields = list_display
    list_filter = ('exclusivo_compartido', 'tipo')
