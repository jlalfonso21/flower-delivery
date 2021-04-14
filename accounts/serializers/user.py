from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accounts.serializers.l10n import MunicipalitySerializer, ProvinceSerializer


class UserMiniSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class UserShortSerializer(UserMiniSerializer):
    phone = SerializerMethodField(method_name='get_phone')
    municipality = SerializerMethodField(method_name='get_mun')
    province = SerializerMethodField(method_name='get_prov')

    class Meta:
        model = User
        fields = UserMiniSerializer.Meta.fields + ['phone', 'email', 'municipality', 'province']

    def get_phone(self, obj):
        return obj.profile.phone

    def get_mun(self, obj):
        return MunicipalitySerializer(obj.profile.mun).data

    def get_prov(self, obj):
        return ProvinceSerializer(obj.profile.mun.provincia).data


class UserFullSerializer(UserShortSerializer):
    ci = SerializerMethodField(method_name='get_ci')

    class Meta:
        model = User
        fields = UserShortSerializer.Meta.fields + ['ci']

    def get_ci(self, obj):
        return obj.profile.ci
