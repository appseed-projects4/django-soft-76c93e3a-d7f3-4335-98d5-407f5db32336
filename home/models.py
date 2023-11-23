# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Corporates User(models.Model):

    #__Corporates User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__Corporates User_FIELDS__END

    class Meta:
        verbose_name        = _("Corporates User")
        verbose_name_plural = _("Corporates User")


class Retail User(models.Model):

    #__Retail User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__Retail User_FIELDS__END

    class Meta:
        verbose_name        = _("Retail User")
        verbose_name_plural = _("Retail User")


class Products(models.Model):

    #__Products_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Orders(models.Model):

    #__Orders_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    retailer = models.CharField(max_length=255, null=True, blank=True)
    fulfillment = models.CharField(max_length=255, null=True, blank=True)

    #__Orders_FIELDS__END

    class Meta:
        verbose_name        = _("Orders")
        verbose_name_plural = _("Orders")


class Payments(models.Model):

    #__Payments_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Payments_FIELDS__END

    class Meta:
        verbose_name        = _("Payments")
        verbose_name_plural = _("Payments")


class Geo Zones(models.Model):

    #__Geo Zones_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Geo Zones_FIELDS__END

    class Meta:
        verbose_name        = _("Geo Zones")
        verbose_name_plural = _("Geo Zones")



#__MODELS__END
