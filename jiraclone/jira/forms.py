from django.forms import ModelForm
from .models import Story

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description', 'status', 'points', 'due_date', 'type']
