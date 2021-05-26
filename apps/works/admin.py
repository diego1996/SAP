from django.contrib import admin
from apps.works.models import Work, WorkCoordinate, Secretary, WorkState, WorkImage


# Register your models here.


class WorkCoordinateAdminInline(admin.StackedInline):
    model = WorkCoordinate
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


class WorkImageAdminInline(admin.TabularInline):
    model = WorkImage
    extra = 1
    suit_classes = 'suit-tab suit-tab-images'


@admin.register(WorkImage)
class WorkImageAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkCoordinate)
class WorkCoordinateAdmin(admin.ModelAdmin):
    pass


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract_id', 'year', 'total_value', 'secretary', 'progress_work', 'actual_work_state')
    list_filter = ('secretary', 'year', 'actual_work_state')
    search_fields = ('year', 'secretary__name', 'secretary__email', 'contract_object', 'pqr')
    inlines = (WorkCoordinateAdminInline, WorkImageAdminInline)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'contract_id',
                'year',
                'contract_object',
                'total_value',
                'progress_work',
                'pqr',
                'secretary',
                'actual_work_state',
            ]
        }),
    ]
    suit_form_tabs = (
        ('general', 'General'),
        ('images', 'Imágenes de la obra'),
    )


@admin.register(Secretary)
class SecretaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'icon')
    list_filter = ()
    search_fields = ('name', 'email')


@admin.register(WorkState)
class WorkStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ()
    search_fields = ('name',)
