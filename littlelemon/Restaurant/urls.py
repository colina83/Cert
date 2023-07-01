from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',views.index,name='index'),
    path('menu-items/',views.MenuItemsView.as_view(),name='menu'),
    path('menu-items/<int:pk>/',views.SingleMenuItemView.as_view(),name='single_menu_item'),
    path('message/',views.msg,name='msg'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    ]