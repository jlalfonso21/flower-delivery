from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accounts.serializers.l10n import MunicipalitySerializer
from store.models import Store


class StoreShortSerializer(ModelSerializer):
    municipality = SerializerMethodField(method_name='get_mun')

    class Meta:
        model = Store
        fields = ['id', 'name', 'municipality', 'phone', 'email', 'website']

    def get_mun(self, obj):
        return MunicipalitySerializer(obj.mun).data if obj.mun is not None else None


class StoreSerializer(StoreShortSerializer):
    class Meta:
        model = Store
        fields = StoreShortSerializer.Meta.fields + ['slogan', 'primary_color', 'secondary_color']
        # TODO: add GIS_INFO
