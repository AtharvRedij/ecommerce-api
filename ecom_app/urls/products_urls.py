from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ecom_app.views import products_views as views

router = DefaultRouter()

router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
