from rest_framework.generics import ListAPIView

from store.models import Product
from store.serializers.product import ProductShortSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductShortSerializer
    queryset = Product.objects.all()
