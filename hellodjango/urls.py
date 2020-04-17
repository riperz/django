"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pypymusic import views
from pybox import views as pybox_views
from pypymusic.admin import admin_site
from todoum import views as todoum_views

urlpatterns = [
    path('admin/', admin_site.urls),
    path('hello/', views.hello),
    path('thanks/<str:name>/', pybox_views.thanks, name='thanks'),
    path('register/', pybox_views.user_register, name='user-registration'),
    path('player/registration/<int:region_id>/', todoum_views.player_registration, name='player-registration'),
]