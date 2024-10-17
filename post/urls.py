from . import views
from django.urls import path

urlpatterns = [
    path('resource_create/',
         views.resource_create, name='resource_create'),
    path('resource_list/',
         views.resource_list, name='resource_list'),
    path('user_posts_list/', views.user_posts_list,
         name='user_posts_list'),
    path('<slug:slug>/resource_preview',
         views.resource_preview, name='resource_preview'),
    path('<slug:slug>/delete_resource/',
         views.resource_delete, name='resource_delete'),
    path('<slug:slug>/resource_detail',
         views.resource_detail, name='resource_detail'),
    path('<slug:slug>/like/',
         views.like_resource, name='like_resource'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_resource/<int:resource_id>',
         views.resource_edit, name='resource_edit'),

    path('', views.home_page, name='home'),
]
