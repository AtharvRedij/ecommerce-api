from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'is_admin']

    is_admin = serializers.SerializerMethodField(read_only=True)

    def get_is_admin(self, user):
        return user.is_staff
