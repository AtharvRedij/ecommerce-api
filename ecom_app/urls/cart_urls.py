from django.urls import path

from ecom_app.views import cart_views as views

urlpatterns = [
    path('', views.handle_cart, name='handle-cart'),
]
