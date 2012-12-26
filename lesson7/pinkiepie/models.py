# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Pie(models.Model):
    name = models.CharField(_('Name'), max_length=255, default='')
    components = models.ManyToManyField('Component', null=True, blank=True)

    class Meta:
        verbose_name = _('Pie')
        verbose_name_plural = _('Pies')

    def __unicode__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(_('Name'), max_length=255, default='')

    class Meta:
        verbose_name = _('Pie component')
        verbose_name_plural = _('Pie components')

    def __unicode__(self):
        return self.name


class Deliveryman(models.Model):
    name = models.CharField(_('Name'), max_length=255, default='')

    class Meta:
        verbose_name = _('Delivery man')
        verbose_name_plural = _('Delivery men')

    def __unicode__(self):
        return self.name


class Order(models.Model):
    MOSCOW, PENZA, OMSK, EQVESTRIA = range(4)
    CITIES = (
        (MOSCOW, _('Moscow')),
        (PENZA, _('Penza')),
        (OMSK, _('Omsk')),
        (EQVESTRIA, _('Eqvestria'))
        )
    city = models.PositiveSmallIntegerField(_('City'), choices=CITIES, default=PENZA)
    address = models.TextField(_('Address'), default='', blank=True)
    deliveryman = models.ForeignKey(Deliveryman, blank=True, null=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __unicode__(self):
        return u'City: %s, Address: %s' % (self.city, self.address)


class OrderItem(models.Model):
    pie = models.ForeignKey(Pie, blank=True, null=True, verbose_name='Pie')
    quantity = models.PositiveIntegerField('Quantity', default=0)
    order = models.ForeignKey(Order, blank=True, null=True)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __unicode__(self):
        return u'Pie: %s, Quantity: %s, Order: %s' % (self.pie, self.quantity, self.order.deliveryman.name)
