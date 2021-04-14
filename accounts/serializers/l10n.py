from l10n_cuba.models import Municipio, Provincia
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class MunicipalitySerializer(ModelSerializer):
    name = SerializerMethodField(method_name='get_name')

    class Meta:
        model = Municipio
        fields = ['id', 'name']

    def get_name(self, obj):
        return obj.nombre


class ProvinceSerializer(ModelSerializer):
    name = SerializerMethodField(method_name='get_name')
    short_name = SerializerMethodField(method_name='get_short_name')

    class Meta:
        model = Provincia
        fields = ['id', 'name', 'short_name']

    def get_name(self, obj):
        return obj.nombre

    def get_short_name(self, obj):
        return obj.nombre_corto


class ProvinceDetailedSerializer(ProvinceSerializer):
    class Meta:
        fields = ProvinceSerializer.Meta.fields + ['municipios']
