
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart_page/', views.show_cart, name='show_cart'),
    path('add_page', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<pk>,', views.remove_item, name='remove_item'),
    path('checkout', views.check_out, name='check_out'),
]
