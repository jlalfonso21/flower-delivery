from rest_framework.generics import ListAPIView

from accounts.serializers.user import *


class ListUserAPIView(ListAPIView):
    serializer_class = UserShortSerializer
    queryset = User.objects.all()

