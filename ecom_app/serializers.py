from django.contrib.auth.models import User
from rest_framework import serializers

from ecom_app.models import Cart, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'is_admin']

    is_admin = serializers.SerializerMethodField(read_only=True)

    def get_is_admin(self, user):
        return user.is_staff


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity']


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ViewCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity', 'product']

    product = SimpleProductSerializer()
