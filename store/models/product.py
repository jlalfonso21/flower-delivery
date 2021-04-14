from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), max_length=255)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=9, decimal_places=2)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)
    tags = models.ManyToManyField(to='store.Tag', related_name='products')
    store = models.ForeignKey(to='store.Store', on_delete=models.CASCADE,
                              related_name='product_of', verbose_name=_('Store'))
    main_image = models.ForeignKey(to='store.ProductImage', on_delete=models.CASCADE, related_name='main_image_of',
                                   verbose_name=_('Main Image'), null=True)

    def get_rating_number(self):
        if self.ratings.count() == 0:
            return 0
        total = sum(i.rating for i in self.ratings.all())
        return total / self.ratings.count()

    def __str__(self):
        return self.name + ' - ' + self.store.name


class Tag(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=32)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(to='store.Product', on_delete=models.CASCADE, related_name='images',
                                verbose_name=_('Product'))
    image = models.ImageField(verbose_name=_('Image'), upload_to='product_images/',
                              height_field='height', width_field='width')
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return 'Image of' + self.product.name
