from rest_framework import viewsets

from ecom_app.models import Product
from ecom_app.serializers import ProductSerializer
from ecom_app.permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
