from django.urls import path
from . import views

urlpatterns = [
    path('home', views.base),
    path('', views.home)

]
