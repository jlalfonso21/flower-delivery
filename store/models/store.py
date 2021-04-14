from django.db import models
from django.utils.translation import gettext_lazy as _


class Store(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    owner = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='stores', verbose_name=_('Owner'))
    mun = models.ForeignKey(to='l10n_cuba.Municipio', on_delete=models.SET_NULL,
                            related_name='stores', verbose_name=_('Municipality'), null=True)
    phone = models.PositiveIntegerField(verbose_name=_('Phone Number'), unique=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True)
    slogan = models.TextField(verbose_name=_('Slogan'), max_length=255, null=True)
    primary_color = models.CharField(verbose_name=_('Primary Color'), max_length=10, null=True, blank=True)
    secondary_color = models.CharField(verbose_name=_('Secondary Color'), max_length=10, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Active?'), default=True)

    # TODO: add GIS_INFO

    def __str__(self):
        return self.name
