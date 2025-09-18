from django.views.generic import DetailView
from .models import Question

class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"
