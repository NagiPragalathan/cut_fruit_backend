from rest_framework import viewsets
from base.models.vendor import VendorItems
from base.serializers.vendor import VendorSerializer
from rest_framework.permissions import IsAuthenticated

class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorItems.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]