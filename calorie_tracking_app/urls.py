from django.urls import path
from calorie_tracking_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_date/<str:date>/', views.delete_date, name='delete_date'),
    path('manage_meals/<str:date>/', views.manage_meals, name="manage_meals"),
    path('edit_facts/<int:id>/', views.edit_meal, name="edit_facts"),
    path('delete_meal/<int:id>/', views.delete_meal, name="delete_meal"),

]