from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ecom_app.models import Cart
from ecom_app.serializers import CartSerializer


def create_or_update_cart(request):
    user_id = request.user.id
    product_id = request.data['product_id']
    quantity = request.data['quantity']

    if quantity <= 0:
        raise serializers.ValidationError(
            'Quantity must be greater than zero')

    try:

        cart_item = Cart.objects.filter(
            user_id=user_id,
            product_id=product_id
        )

        if cart_item.exists():
            cart_item = cart_item.first()
            cart_item.quantity += quantity
            cart_item.save()

        else:

            cart_item = Cart.objects.create(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity
            )

        serializer = CartSerializer(cart_item)

        return Response(serializer.data)

    except Exception as ex:

        return Response({"error_message": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def handle_cart(request):

    if request.method == 'GET':
        return Response('get called')

    elif request.method == 'POST':
        return create_or_update_cart(request)
