from django.db import models

# Create your models here.


class WorkState(models.Model):
    name = models.CharField(verbose_name='Nombre de un estado de un contrato', max_length=100)

    class Meta:
        verbose_name = 'Estado de la obra'
        verbose_name_plural = 'Estados de las obras'

    def __str__(self):
        return self.name


class Secretary(models.Model):
    name = models.CharField(verbose_name='Nombre de la secretaría', max_length=100)
    email = models.EmailField(verbose_name='Email de la secretaría', max_length=100)
    icon = models.ImageField(verbose_name='Icono de la secretaría', upload_to='uploads/marker_icons/secretary/')

    class Meta:
        verbose_name = 'Secretaría'
        verbose_name_plural = 'Secretarías'

    def __str__(self):
        return self.name


class Work(models.Model):
    contract_id = models.CharField(verbose_name='ID de Contrato', max_length=100)
    year = models.PositiveIntegerField(verbose_name='Año de la obra')
    contract_object = models.TextField(verbose_name='Objeto del contrato', max_length=900)
    total_value = models.CharField(verbose_name='Valor total', max_length=100)
    secretary = models.ForeignKey(Secretary, verbose_name='Secretaría Responsable', on_delete=models.PROTECT)
    progress_work = models.PositiveIntegerField(verbose_name='% de Avance de la Obra')
    actual_work_state = models.ForeignKey(WorkState, verbose_name='Estado actual', on_delete=models.PROTECT)
    pqr = models.TextField(verbose_name='Petición, Queja o Reclamo', max_length=900)

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'

    def __str__(self):
        return f'{self.contract_id}'


class WorkCoordinate(models.Model):
    work = models.ForeignKey(Work, verbose_name='Obra a la que pertenece', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Nombre', max_length=100, default='Coordenadas de la obra')
    latitude = models.FloatField(verbose_name='Latitud')
    longitude = models.FloatField(verbose_name='Longitud')

    class Meta:
        verbose_name = 'Coordenada de la obra'
        verbose_name_plural = 'Coordenadas de las obras'

    def __str__(self):
        return f'{self.name}-{self.work}-{self.latitude}-{self.longitude}'


class WorkImage(models.Model):
    work = models.ForeignKey(Work, verbose_name='Obra a la que pertenece', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Imágen', upload_to='uploads/gallery/works/')

    class Meta:
        verbose_name = 'Imágen de la obra'
        verbose_name_plural = 'Imagenes de las obras'

    def __str__(self):
        return f'{self.id}-{self.work}'
