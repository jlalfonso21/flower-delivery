from django.db import models
from django.utils.translation import gettext_lazy as _

RATINGS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class Rating(models.Model):
    user = models.ForeignKey(to='auth.User', on_delete=models.SET_NULL,
                             verbose_name=_('User'), null=True, related_name='ratings')
    product = models.ForeignKey(to='store.Product', on_delete=models.CASCADE,
                                verbose_name=_('Product'), related_name='ratings')
    comment = models.TextField(verbose_name=_('Comment'), max_length=255)
    as_anon = models.BooleanField(verbose_name=_('Anonymous'), default=False)
    rating = models.SmallIntegerField(verbose_name=_('Rating'), default=3, choices=RATINGS)
    created_on = models.DateTimeField(verbose_name=_('Created on'), auto_now_add=True)

    def __str__(self):
        return str(self.rating) + ' - ' + self.product.name
