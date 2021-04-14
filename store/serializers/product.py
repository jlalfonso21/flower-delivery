from rest_framework.serializers import ModelSerializer, SerializerMethodField

from socials.serializers.rating import RatingSerializer
from store.models import Product, Tag, ProductImage
from store.serializers.store import StoreShortSerializer


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'width', 'height']


class ProductShortSerializer(ModelSerializer):
    rating = SerializerMethodField(method_name='get_rating')
    tags = TagSerializer(many=True)
    store = StoreShortSerializer()
    main_image = ImageSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'main_image', 'price', 'store', 'rating', 'tags']

    def get_rating(self, obj):
        return obj.get_rating_number()


class ProductSerializer(ProductShortSerializer):
    ratings = RatingSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ProductShortSerializer.Meta.fields + ['ratings', 'images', 'description']
