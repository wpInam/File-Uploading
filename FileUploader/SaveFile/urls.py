from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # For index page or default page
    path('upload/', views.upload_file, name='upload_file'),
]