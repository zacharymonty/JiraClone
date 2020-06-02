from .forms import StoryForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

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
            return HttpResponseRedirect("/success/")
        return render(request, self.template_name, {"form": form})
