
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('accout_page/', views.show_account, name='show_account'),
    path('logout_page/', views.log_out, name='logout')
]