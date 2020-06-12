from django.shortcuts import render
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers
import random
from .models import Image

from .serializers import ImageSerializer


class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.data)
        image_serializer = ImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(image_serializer.errors)
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictCOVID19Score(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id, format=None):
        obj = None
        try:
            obj = Image.objects.get(pk=id)
        except Image.DoesNotExist:
            return Response({"error": "invalid_id"})
        res = {
            "name": obj.__str__()
        }
        if obj.prediction() == None:
            res["score"] = random.random() * 100
            obj.score = res["score"]
            obj.save()
        else:
            res["score"] = obj.prediction()
        return Response(res)
