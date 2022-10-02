from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('new_game', views.new_game),
    path('scorecard', views.scorecard),
]