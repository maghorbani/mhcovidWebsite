from .models import Image
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer
import random

# Image Viewset


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ImageSerializer

    def get_queryset(self):
        if (self.request.user.is_authenticated):
            return self.request.user.images.all()
        else:
            return Image.objects.all()

    def perform_create(self, serializer):
        # print(serializer.validated_data['score'])
        if (self.request.user.is_authenticated):
            serializer.save(owner=self.request.user,
                            score=random.random() * 100)
        else:
            serializer.save(score=random.random() * 100)
