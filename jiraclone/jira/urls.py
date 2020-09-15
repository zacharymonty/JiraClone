from .views import NewStoryView, HomeView, StoryView
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("new-story/", NewStoryView.as_view()),
    path("story-detail/<int:story_id>", StoryView.as_view(), name="story_detail"),
]