from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from l10n_cuba.models import Municipio, Provincia


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    mun = models.ForeignKey(to='l10n_cuba.Municipio', on_delete=models.SET_NULL,
                            related_name='users', verbose_name=_('Municipality'), null=True)
    phone = models.PositiveIntegerField(verbose_name=_('Phone Number'), unique=True, null=True)
    ci = models.CharField(verbose_name=_('Identification Card'), max_length=11, null=True)

    # TODO: add gis_info field

    def __str__(self):
        return "{}'s Profile".format(self.user.username)


@receiver(post_save, sender=User)
def on_user_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
