from django.urls import path
from calorie_tracking_app import views

urlpatterns = [
    path('', views.index, name='index')
]