# from django.urls  import path
# from .views import ImageUploadView, PredictCOVID19Score

# app_name ="records"
# urlpatterns = [
#         path('', ImageUploadView.as_view()),
#         path('predict/<int:id>/', PredictCOVID19Score.as_view(),name="prediction")
# ]

from rest_framework import routers
from .api import ImageViewSet

router = routers.DefaultRouter()
router.register('images', ImageViewSet, basename='images')

urlpatterns = router.urls
