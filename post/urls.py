from . import views
from django.urls import path

urlpatterns = [
    path('resource_list/', views.resource_list, name='resource_list'),
    path('<slug:slug>/', views.resource_detail, name='resource_detail'),
    path('', views.ResourceList.as_view(), name='home'),
]