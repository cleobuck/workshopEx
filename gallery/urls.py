from django.urls import path
from django.http import HttpResponse

from . import views

app_name="gallery"

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('post/', views.CreatePostView.as_view(), name='add_post')
]
