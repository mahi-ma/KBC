from .models import Question
from random import randint
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'firstBeat/index.html'
    context_object_name = "propane"

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'firstBeat/details.html'

