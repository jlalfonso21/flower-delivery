from django.urls import path

from api.views.product import ProductListAPIView
from api.views.rating import RatingAPIView
from api.views.store import StoreListAPIView
from api.views.user import ListUserAPIView
from rest_framework_simplejwt import views as jwt_views

app_name = 'api'
urlpatterns = [

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', ListUserAPIView.as_view(), name='user-list'),
    path('ratings/', RatingAPIView.as_view(), name='ratings'),
    path('stores/', StoreListAPIView.as_view(), name='store-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]
