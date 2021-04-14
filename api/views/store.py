from rest_framework.generics import ListAPIView

from store.models import Store
from store.serializers.store import StoreSerializer


class StoreListAPIView(ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
