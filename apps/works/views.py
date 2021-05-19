import json
import urllib.parse

from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.contrib import admin
# Create your views here.
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from apps.works.models import Work


@staff_member_required
def custom_admin_view(request):
    context = admin.site.each_context(request)
    context.update({
        'title': 'Vista personalizada',
    })

    template = 'admin/custom_view.html'
    return render(request, template, context)


def home(request):
    context = admin.site.each_context(request)
    context.update({
        'title': 'Bienvenidos a la app de Frentes de Obras de Villavicencio',
    })

    template = 'mapa/index.html'
    return render(request, template, context)


def pqr(request, work_id):
    context = admin.site.each_context(request)
    work = Work.objects.filter(id=work_id).values()
    context.update({
        'title': 'Formulario PQR',
        'work': work
    })
    template = 'mapa/pqr.html'
    return render(request, template, context)


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        if not body_unicode:
            return HttpResponseBadRequest("No body request")
        body = json.loads(body_unicode)
        req_email = body.get('email', None)
        req_message = body.get('message', None)
        if (None or '') in (req_email, req_message):
            return HttpResponseBadRequest("Body incomplete")
        body = render_to_string(
            'email/email-template.html',
            {
                'email': req_email,
                'message': urllib.parse.unquote(req_message).replace("+", " "),
            }
        )
        email = EmailMessage(
            subject='Nueva Solicitud de Gobierno Contigo',
            body=body,
            from_email=req_email,
            to=['correspondencia@villavicencio.gov.co', 'giver.cupaja@gmail.com']
        )
        email.content_subtype = "html"
        email.send()
        return HttpResponse("Correo enviado")
    else:
        return HttpResponseBadRequest("Method not allowed")
