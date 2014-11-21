from django.http import HttpResponse
from django.shortcuts import render
from CookingBuddy.models import Event
# Create your views here.


def index(request):
    context_dict = {}
    return render(request, 'cooking_buddy/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'cooking_buddy/about.html', context_dict)


def salisbury_steak(request):
    context_dict = {}
    return render(request, 'cooking_buddy/salisbury_steak.html', context_dict)


def log_utterance(request):
    """Save the log of the user's utterance to the database"""
    if request.method == 'POST':
        timestamp = request.POST['timestamp']
        action = request.POST['action']
        confidence = request.POST['asrResults[0][confidence]']
        utterance = request.POST['asrResults[0][transcript]']
        current_step = request.POST['current_step']

        event = Event(timestamp=timestamp, confidence=confidence,
                      utterance=utterance, current_step=current_step, action=action)
        event.save()

    return HttpResponse()