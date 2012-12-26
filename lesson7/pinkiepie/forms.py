# coding: utf-8
from __future__ import unicode_literals
from .models import Order, Deliveryman, OrderItem
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('city', 'address',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'Order'
        self.helper.add_input(Submit('', 'Submit'))

    def save(self, *args, **kwargs):
        self.instance.deliveryman = Deliveryman.objects.get(name='user1')
        return super(OrderForm, self).save(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['city'] == Order.PENZA and not self.cleaned_data['address'].strip():
            raise forms.ValidationError('Please')
        return self.cleaned_data


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'IWannaPie'
        self.helper.add_input(Submit('', 'Submit'))
