from django.urls import path
from .views import *

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),
]
