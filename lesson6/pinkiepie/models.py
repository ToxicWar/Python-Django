from django.db import models


class Pie(models.Model):
    name = models.CharField('Name', max_length=255, default='')
    components = models.ManyToManyField('Component', null=True, blank=True)

    class Meta:
        verbose_name = 'Pie'
        verbose_name_plural = 'Pies'

    def __unicode__(self):
        return self.name


class Component(models.Model):
    name = models.CharField('Name', max_length=255, default='')

    class Meta:
        verbose_name = 'Pie component'
        verbose_name_plural = 'Pie components'

    def __unicode__(self):
        return self.name


class Deliveryman(models.Model):
    name = models.CharField('Name', max_length=255, default='')

    class Meta:
        verbose_name = 'Delivery man'
        verbose_name_plural = 'Delivery men'

    def __unicode__(self):
        return self.name


class Order(models.Model):
    address = models.TextField('Address', default='')
    deliveryman = models.ForeignKey(Deliveryman, blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __unicode__(self):
        return u'Address: %s' % self.address


class OrderItem(models.Model):
    pie = models.ForeignKey(Pie, blank=True, null=True, verbose_name='Pie')
    quantity = models.PositiveIntegerField('Quantity', default=0)
    order = models.ForeignKey(Order, blank=True, null=True)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __unicode__(self):
        return u'Pie: %s' % self.pie
