from django.urls import path
from .views import *

urlpatterns = [
    path('get', get_assigments),
]