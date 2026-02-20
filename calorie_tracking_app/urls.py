from django.urls import path
from hello_world_app import views

urlpatterns = [
    path('home/', views.index, name='index')
]