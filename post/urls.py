from . import views
from django.urls import path

urlpatterns = [
    path('resource_create/', views.resource_create, name='resource_create'),
    path('resource_list/', views.resource_list, name='resource_list'),
    path('<slug:slug>/', views.resource_detail, name='resource_detail'),
    path('', views.home_page, name='home'),
]