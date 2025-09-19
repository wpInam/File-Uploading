from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'), # For index page or default page
]