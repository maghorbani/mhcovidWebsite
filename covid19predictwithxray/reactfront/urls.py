from django.urls import re_path, path
from .views import index

urlpatterns = [
    # path(r'^.*$', index, name="home"),
    path('', index),
    # path('aboutus/', index),
    re_path('.*/', index, name='index'),
]
