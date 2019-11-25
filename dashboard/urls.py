from django.conf import settings

from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate/', views.populate, name='populate'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('search/', views.search, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)