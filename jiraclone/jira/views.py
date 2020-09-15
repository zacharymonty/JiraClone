from .forms import StoryForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Story
import logging

Story = Story

logger = logging.getLogger(__name__)

class HomeView(View):
    template_name = 'home.html'


    def get(self, request, *args, **kwargs):
        stories = Story.objects.all()
        # stories = stories.__dict__
        return render(request, "home.html", {"stories": stories})

class NewStoryView(FormView):
    template_name = 'story.html'
    form_class = StoryForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            # title = form.cleaned_data['title']
            # description = form.cleaned_data['description']
            # status = form.cleaned_data['status']
            # points = form.cleaned_data['points']
            # due_date = form.cleaned_data['due_date']
            # type = form.cleaned_data['type']
            # story = Story()
            # story.save(title=title, description=description, status=status, points=points, due_date=due_date, type=type)

            form.save()

            return HttpResponseRedirect("/")
        else:
            logger.info("Form is invalid")


        return render(request, self.template_name, {"form": form})

class StoryView(View):
    template_name = 'story_detail.html'

    def get(self, request, story_id):
        story = Story.objects.get(id=story_id)
        return render(request, self.template_name, {"story": story})