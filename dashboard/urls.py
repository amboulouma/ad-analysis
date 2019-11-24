from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate/', views.populate, name='populate'),
    path('fetch_all/', views.fetch_all, name='fetch_all'),
]