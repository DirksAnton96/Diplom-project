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

from app.views import home_page_view, show_place_view, users_coworking_page_view, create_coworkings_view,show_coworking_view, update_coworking_view, delete_coworking_view, show_all_coworkings, show_all_review_view, show_user_reviews_view, show_review_view, create_review_view, update_review_view, delete_review_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include("django.contrib.auth.urls")),
    
    path("", home_page_view, name="home-place"),
    path("place/<place_id>", show_place_view, name="show-place"),
    path("coworkingspace/<username>/places", users_coworking_page_view, name="list-users-coworkings"),
    path("coworkingspace/create", create_coworkings_view, name="create-user-coworking"),
    path("coworkingspace/<coworking_id>", show_coworking_view, name="show-request-coworking"),
    path("coworkingspace/update/<coworking_id>", update_coworking_view, name="update-coworking-request" ),
    path("coworkingspace/delete/<coworking_id>", delete_coworking_view, name="delete-coworking-request" ),
    path("coworkingspace/all/places_all", show_all_coworkings, name="show-all-coworkings" ),
    path("review/all/reviews", show_all_review_view, name="show-all-review" ),
    path("review/list/<username>/reviews", show_user_reviews_view, name="show-user-reviews"),
    path("review/create", create_review_view, name="create-review-view"),
    path("review/list/<review_id>", show_review_view, name="show-review-view"),
    path("review/list/update/<review_id>", update_review_view, name="update-review-view" ),
    path("review/list/delete/<review_id>", delete_review_view, name="delete-review-view" ),    
]
