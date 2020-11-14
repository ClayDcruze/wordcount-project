from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('counfffft/', views.count, name='count')
]
