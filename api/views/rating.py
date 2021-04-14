from rest_framework.generics import ListAPIView

from socials.models import Rating
from socials.serializers.rating import RatingSerializer


class RatingAPIView(ListAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
