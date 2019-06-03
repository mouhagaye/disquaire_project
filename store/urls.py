from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('listing',views.listing),
    path('<int:album_id>',views.details),
    path('search',views.search),
]