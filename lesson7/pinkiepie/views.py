# coding: utf-8
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView
from .models import Pie, Order, Deliveryman, OrderItem
from django.http import Http404
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse_lazy
from django.forms.models import inlineformset_factory
from .forms import OrderForm, OrderItemForm


class PieListView(ListView):
    model = Pie
    template_name = 'index.html'
    template_context_name = 'pie_list'

pie_list = PieListView.as_view()


class ApplePieListView(PieListView):
    def get_queryset(self):
        return super(ApplePieListView, self).get_queryset().filter(name__icontains='блочный')

apple = ApplePieListView.as_view()


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order.html'
    success_url = reverse_lazy('home')


class CreateOrderItemView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'order.html'
    success_url = reverse_lazy('home')

create_order = CreateOrderView.as_view()

IWannaPie = CreateOrderItemView.as_view()
