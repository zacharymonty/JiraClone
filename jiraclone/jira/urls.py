from .views import StoryView, HomeView
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("new-story/", StoryView.as_view())
]