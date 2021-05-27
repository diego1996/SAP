"""SAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import SAP.strings as const
from django.conf.urls.static import static
from django.urls import path, include
from django.utils.html import format_html
from django.views.generic import RedirectView
from SAP import settings
from apps.works import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # django select
    path('select2/', include('django_select2.urls')),

    path('admin/custom/', views.custom_admin_view),
    # Documentation url for menu documentation link
    path('admin/custom2/', RedirectView.as_view(url='https://www.diegoasencio.co/'), name='app-admindocs-docroot'),

    path('', views.home, name='home'),

    path('', include('apps.works.urls')),
    path('', include('apps.street_lighting.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = format_html("{name}", name=const.APP_NAME_VERSION)
