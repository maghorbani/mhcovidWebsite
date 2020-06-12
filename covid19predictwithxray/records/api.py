from .models import Image
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
# from MHCovid import MHCovid
from .MHCovid import MHCovid
import os
import matplotlib


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

        model_obj = None
        if (self.request.user.is_authenticated):
            model_obj = serializer.save(owner=self.request.user)
        else:
            model_obj = serializer.save()

        matplotlib.use('agg')
        matplotlib.pyplot.switch_backend('Agg')

        fileName = model_obj.file.name
        mh = MHCovid()
        model = mh.generateModel()
        model.load_weights(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'cmodel.h5'))
        dirp = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..'))
        fileName = os.path.join(dirp, 'media', fileName)
        pr = mh.predict(model, fileName)

        if (self.request.user.is_authenticated):
            serializer.save(owner=self.request.user,
                            score=pr*100)
        else:
            serializer.save(score=pr*100)

    def retrieve(self, request, pk=None):
        queryset = Image.objects.all()
        image = get_object_or_404(queryset, pk=pk)
        # print(request.query_params)
        dirp = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..'))
        fileName = os.path.join(dirp, 'media', image.file.name)
        if('imagefile' in request.query_params):
            image_data = open(fileName, "rb").read()
            return HttpResponse(image_data, content_type="image/png")

        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def list(self, request):
        queryset = Image.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ImageSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)
