from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem('Elementos', children=[
            ChildItem('Luminarias', 'street_lighting.luminaria'),
            ChildItem('Postes', 'street_lighting.poste'),
            ChildItem('Redes', 'street_lighting.red'),
            ChildItem('Camaras y canalizaciones', 'street_lighting.camara'),
            ChildItem('Transformadores', 'street_lighting.transformador'),
        ], icon='fa fa-slideshare'),
        ParentItem('Hojas de vida', children=[
            ChildItem('Usuarios', 'cv.workstate'),
        ], icon='fa fa-slideshare'),
        ParentItem('Usuarios', children=[
            ChildItem(model='auth.user'),
            ChildItem('Grupos de Usuarios', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Otras opciones', children=[
            ChildItem('Cambiar contraseña', url='admin:password_change'),
            ChildItem('Abrir Google', url='https://google.com', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )

    def ready(self):
        super(SuitConfig, self).ready()

        # DO NOT COPY FOLLOWING LINE
        # It is only to prevent updating last_login in DB for demo app
        self.prevent_user_last_login()

    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
        user_logged_in.disconnect(update_last_login)