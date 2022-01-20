from django.urls import path
from . import views

app_name = 'media'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:picture_pk>', views.delete, name='delete'),
]