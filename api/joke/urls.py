from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random_page', views.random_page, name='random_page'),

]
