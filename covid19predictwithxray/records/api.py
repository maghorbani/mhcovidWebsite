from .models import Image
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer
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
