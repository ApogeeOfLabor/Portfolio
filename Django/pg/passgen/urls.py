from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('rooms/', rooms),
    path('services/', services),

]