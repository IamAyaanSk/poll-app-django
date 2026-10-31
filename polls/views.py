from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id: int):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question not found!")
    return render(request, "polls/detail.html", {"question": question})

    return HttpResponse(f"You're looking at question {question_id}.")


def results(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}.")
