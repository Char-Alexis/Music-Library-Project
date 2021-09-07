from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('song/', views.SongList.as_view()),
]