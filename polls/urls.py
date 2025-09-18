from django.urls import path

from . import views
#from . import view_detail

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]

"""
urlpatterns = [
    # Home page : /polls/
    path('', views.index, name='index'),
    # Detail page: /polls/question_id=1/
    path('<int:question_id>/', views.detail, name='detail'),
    # Results: /polls/question_id/results/
    path('<int:question_id>/results', views.results, name='results'),
    # Vote: /polls/question_id/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
