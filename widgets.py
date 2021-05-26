from django.conf import settings
from django.forms import forms
from django.templatetags.static import static


class Bootstrap4Select(object):
    def build_attrs(self, extra_attrs=None, **kwargs):
        attrs = super(Bootstrap4Select, self).build_attrs(extra_attrs, **kwargs)
        attrs.setdefault('data-theme', 'bootstrap')
        return attrs

    def _get_media(self):

        return forms.Media(
            js=(
                settings.SELECT2_JS,
                static('django_select2/django_select2.js'),
            ),
            css={'screen': (
                settings.SELECT2_CSS,
                # static('css/select2-bootstrap.css'),
                '//cdnjs.cloudflare.com/ajax/libs/select2-bootstrap-theme/0.1.0-beta.6/select2-bootstrap.min.css',)}
        )

    media = property(_get_media)
