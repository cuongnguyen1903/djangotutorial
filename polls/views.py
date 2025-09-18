from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from .view_detail import DetailView
from .view_index import IndexView
from .view_results import ResultsView

"""
__all__ = [
    #"DetailView",
    #"IndexView",
]
"""
"""
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        #Return the last five published questions.
        return Question.objects.order_by("-pub_date")[:5]    
"""
"""
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
"""
""" Optional DetailView
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["choices"] = self.object.choice_set.all()
        return context
"""
"""
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    """

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question, "error_message": "You didn't choose yet"}
    try:
         #choice_id = request.POST["choice"]
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the voting form
        return render(request, "polls/detail.html", context)
    else:
        #selected_choice.votes = F("votes") + 1
        selected_choice.votes += 1
        selected_choice.save()
    #return render(request, "polls/results.html", {"question": question})
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))    

"""
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question, "error_message": "You didn't choose yet"}
    try:
         #choice_id = request.POST["choice"]
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the voting form
        return render(request, "polls/detail.html", context)
    else:
        #selected_choice.votes = F("votes") + 1
        selected_choice.votes += 1
        selected_choice.save()
    #return render(request, "polls/results.html", {"question": question})
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)
"""
