from django.db import models


class Luminaria(models.Model):
    num_unico_rotulo = models.CharField(verbose_name='Numero unico del rotulo', max_length=100)
    latitude = models.CharField(verbose_name='Latitud (coordenada)', max_length=100)
    longitude = models.CharField(verbose_name='Longitud (coordenada)', max_length=100)
    ubicacion = models.CharField(verbose_name='Ubicación', max_length=100, blank=True, null=True)
    tipo_fuente_luminica = models.CharField(verbose_name='Tipo de fuente Luminica', max_length=100, blank=True, null=True)
    potencia = models.CharField(verbose_name='Potencia', max_length=100, blank=True, null=True)
    tipo_luminaria = models.CharField(verbose_name='Tipo de luminaria', max_length=100, blank=True, null=True)
    tipo_balastro = models.CharField(verbose_name='Tipo de balastro', max_length=100, blank=True, null=True)
    valor_perdidas = models.CharField(verbose_name='Valor de las perdidas', max_length=100, blank=True, null=True)
    control_encendido = models.CharField(verbose_name='Control de encendido', max_length=100, blank=True, null=True)
    tipo_espacio_luminado = models.CharField(verbose_name='Tipo de espacio luminado', max_length=100, blank=True, null=True)
    identificacion_transformador = models.CharField(verbose_name='Identificación del transformador de distribución', max_length=100, blank=True, null=True)
    medidor = models.CharField(verbose_name='Medidor', max_length=100, blank=True, null=True)
    nivel_tension = models.CharField(verbose_name='Nivel de tensión', max_length=100, blank=True, null=True)
    horas_diarias_funcionamiento = models.CharField(verbose_name='Horas diaras de funcionamiento', blank=True, null=True, max_length=100)
    costo_unidad_constructiva = models.CharField(verbose_name='Costo de la unidad constructiva', blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Luminaria'
        verbose_name_plural = 'Luminarias'

    def __str__(self):
        return f'{self.num_unico_rotulo}'


class Poste(models.Model):
    num_unico_rotulo = models.CharField(verbose_name='Numero unico del rotulo', max_length=100)
    latitude = models.CharField(verbose_name='Latitud (coordenada)', max_length=100)
    longitude = models.CharField(verbose_name='Longitud (coordenada)', max_length=100)
    ubicacion = models.CharField(verbose_name='Ubicación', max_length=100, blank=True, null=True)
    exclusivo_compartido = models.CharField(verbose_name='Exclusivo/Compartido', max_length=100, blank=True, null=True)
    tipo_material = models.CharField(verbose_name='Tipo de material', max_length=100, blank=True, null=True)
    longitud = models.CharField(verbose_name='Longitud', max_length=100, blank=True, null=True)
    costo_unidad_constructiva = models.CharField(verbose_name='Costo de la unidad constructiva', blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Poste'
        verbose_name_plural = 'Postes'

    def __str__(self):
        return f'{self.num_unico_rotulo}'


class Red(models.Model):
    num_unico_rotulo = models.CharField(verbose_name='Numero unico del rotulo', max_length=100)
    latitude_desde = models.CharField(verbose_name='Latitud desde (coordenada)', max_length=100, blank=True, null=True)
    longitude_desde = models.CharField(verbose_name='Longitud desde (coordenada)', max_length=100, blank=True, null=True)
    latitude_hasta = models.CharField(verbose_name='Latitud hasta (coordenada)', max_length=100, blank=True, null=True)
    longitude_hasta = models.CharField(verbose_name='Longitud hasta (coordenada)', max_length=100, blank=True, null=True)
    direccion = models.CharField(verbose_name='Direccion', max_length=100, blank=True, null=True)
    exclusivo_compartido = models.CharField(verbose_name='Exclusivo/Compartido', max_length=100, blank=True, null=True)
    tipo_material = models.CharField(verbose_name='Tipo de material', max_length=100, blank=True, null=True)
    calibre_conductores = models.CharField(verbose_name='Calibre de conductores', max_length=100, blank=True, null=True)
    tipo_instalacion = models.CharField(verbose_name='Tipo de instalación', max_length=100, blank=True, null=True)
    costo_unidad_constructiva = models.CharField(verbose_name='Costo de la unidad constructiva', blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Red'
        verbose_name_plural = 'Redes'

    def __str__(self):
        return f'{self.num_unico_rotulo}'


class Camara(models.Model):
    num_unico_rotulo = models.CharField(verbose_name='Numero unico del rotulo', max_length=100)
    latitude_desde = models.CharField(verbose_name='Latitud desde (coordenada)', max_length=100, blank=True, null=True)
    longitude_desde = models.CharField(verbose_name='Longitud desde (coordenada)', max_length=100, blank=True, null=True)
    latitude_hasta = models.CharField(verbose_name='Latitud hasta (coordenada)', max_length=100, blank=True, null=True)
    longitude_hasta = models.CharField(verbose_name='Longitud hasta (coordenada)', max_length=100, blank=True, null=True)
    direccion = models.CharField(verbose_name='Direccion', max_length=100, blank=True, null=True)
    exclusivo_compartido = models.CharField(verbose_name='Exclusivo/Compartido', max_length=100, blank=True, null=True)
    cajas_inspeccion = models.CharField(verbose_name='Cajas de inspección', max_length=100, blank=True, null=True)
    ducterias = models.CharField(verbose_name='Ducterias', max_length=100, blank=True, null=True)
    tipo_zona = models.CharField(verbose_name='Tipo de zona', max_length=100, blank=True, null=True)
    costo_unidad_constructiva = models.CharField(verbose_name='Costo de la unidad constructiva', blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Camara y Canalización'
        verbose_name_plural = 'Camaras y Canalizaciones'

    def __str__(self):
        return f'{self.num_unico_rotulo}'


class Transformador(models.Model):
    num_unico_rotulo = models.CharField(verbose_name='Numero unico del rotulo', max_length=100)
    latitude = models.CharField(verbose_name='Latitud (coordenada)', max_length=100)
    longitude = models.CharField(verbose_name='Longitud (coordenada)', max_length=100)
    ubicacion = models.CharField(verbose_name='Ubicación', max_length=100, blank=True, null=True)
    exclusivo_compartido = models.CharField(verbose_name='Exclusivo/Compartido', max_length=100, blank=True, null=True)
    tipo = models.CharField(verbose_name='Tipo', max_length=100, blank=True, null=True)
    capacidad = models.CharField(verbose_name='Capacidad', max_length=100, blank=True, null=True)
    valor_catastral = models.CharField(verbose_name='Valor catastral del terreno', max_length=100, blank=True, null=True)
    area_terreno = models.CharField(verbose_name='Area del terreno', max_length=100, blank=True, null=True)
    costo_unidad_constructiva = models.CharField(verbose_name='Costo de la unidad constructiva', blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Transformador'
        verbose_name_plural = 'Transformadores'

    def __str__(self):
        return f'{self.num_unico_rotulo}'
