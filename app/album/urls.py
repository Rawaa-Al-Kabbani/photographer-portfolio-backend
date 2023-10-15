from django.urls import path
from . import views


urlpatterns = [
    path("", views.album),
    path("categories/", views.categories),
    path("contact/", views.contact),
    path("about/", views.about),
    path("website/", views.website),
]
