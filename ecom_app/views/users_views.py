from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ecom_app.serializers import UserSerializer


def create_user(data, is_staff=False):
    try:

        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=make_password(data['password']),
            is_staff=is_staff
        )

        serializer = UserSerializer(user)
        return Response(serializer.data)

    except KeyError as key_name:

        return Response(f'{key_name} not provided', status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

        return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def register_admin_user(request):
    # here admin means is staff attribute

    return create_user(request.data, is_staff=True)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def register_user(request):
    return create_user(request.data)
