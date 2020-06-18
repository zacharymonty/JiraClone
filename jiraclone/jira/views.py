from .forms import StoryForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .models import Story

class StoryView(FormView):
    template_name = 'story.html'
    form_class = StoryForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            points = form.cleaned_data['points']
            due_date = form.cleaned_data['due_date']
            type = form.cleaned_data['type']
            story = Story()
            story.save(title=title, description=description, status=status, points=points, due_date=due_date, type=type)

            return HttpResponseRedirect("/success/")
        return render(request, self.template_name, {"form": form})
