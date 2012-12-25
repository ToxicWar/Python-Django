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


class PieListView(ListView):
    model = Pie
    template_name = 'index.html'
    template_context_name = 'pie_list'

pie_list = PieListView.as_view()


class ApplePieListView(PieListView):
    def get_queryset(self):
        return super(ApplePieListView, self).get_queryset().filter(name__icontains='блочный')

apple = ApplePieListView.as_view()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        #fields = ('address',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'Order'
        self.helper.add_input(Submit('', 'Submit'))

    def save(self, *args, **kwargs):
        self.instance.deliveryman = Deliveryman.objects.get(name='user1')
        return super(OrderForm, self).save(*args, **kwargs)


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order.html'
    success_url = reverse_lazy('home')

create_order = CreateOrderView.as_view()


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'IWannaPie'
        self.helper.add_input(Submit('', 'Submit'))


class CreateOrderItemView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'order.html'
    success_url = reverse_lazy('home')


IWannaPie = CreateOrderItemView.as_view()
