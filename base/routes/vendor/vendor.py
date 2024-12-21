from rest_framework import viewsets
from base.models.vendor import VendorItems
from base.serializers.vendor import VendorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorItems.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if 'status' in serializer.validated_data and not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to update the status field.")
        
        serializer.save(user=self.request.user)
