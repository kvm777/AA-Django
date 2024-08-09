from django.urls import path
from .views import *

urlpatterns = [
    path("crud/", crudIndex, name="crud-index-page"),
    
]
