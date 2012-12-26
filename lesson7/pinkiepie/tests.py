# coding: utf-8
from __future__ import unicode_literals
from django.test.testcases import TestCase
from .models import Order
from django.utils.translation import ugettext_lazy
from django.test import Client
from django.core.urlresolvers import reverse


class SimpleTest(TestCase):
    def setUp(self):
        self.order = Order()
        self.order.city = Order.PENZA
        self.client = Client()

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code == 200)
        self.assertTrue('order_form' in response.context)
        self.assertTrue(b'10000,0' in response.content)
