from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView
from .models import Pie


def pie_list(request):
    pie_list = Pie.objects.all()
    return TemplateResponse(request, 'index.html', {'pie_list': pie_list})
