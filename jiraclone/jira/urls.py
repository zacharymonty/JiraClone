from .views import StoryView
from django.urls import path

urlpatterns = [
    path("new-story/", StoryView.as_view())
]