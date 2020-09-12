from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.detail_pet, name='detail_pet'),
    path('my_pets', views.my_pets, name='my_pets'),
]