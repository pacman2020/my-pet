from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/', views.my_pets, name='my_pets'),
    path('pet/new/', views.new_pet, name='new_pet'),
    path('pet/<int:pk>/detail/', views.detail_pet, name='detail_pet'),
    path('pet/<int:pk>/edit/', views.edit_pet, name='edit_pet'),
    path('pet/<int:pk>/delete/', views.delete_pet, name='delete_pet'),
]