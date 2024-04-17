"""
URL configuration for coworkingspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path

from app.views import home_page_view, show_place_view, users_coworking_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include("django.contrib.auth.urls")),
    
    path("", home_page_view, name="home-place"),
    path("place/<place_id>", show_place_view, name="show-place"),
    path("coworkingspace/<username>/places", users_coworking_page_view, name="list-users-coworkings"),
]
