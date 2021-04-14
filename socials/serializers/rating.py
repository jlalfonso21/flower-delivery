from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accounts.serializers.user import UserMiniSerializer
from socials.models import Rating


class RatingSerializer(ModelSerializer):
    user = SerializerMethodField(method_name='get_user')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'product', 'comment', 'rating', 'created_on']

    def get_user(self, obj):
        if obj.as_anon:
            return None
        return UserMiniSerializer(obj.user).data
