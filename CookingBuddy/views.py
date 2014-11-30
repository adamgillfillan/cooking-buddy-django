from django.http import HttpResponse
from django.shortcuts import render
from CookingBuddy.models import Event


def index(request):
    context_dict = {}
    return render(request, 'cooking_buddy/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'cooking_buddy/about.html', context_dict)

def recipe(request, recipe):
    context_dict = {"recipe": recipe}
    return render(request, 'cooking_buddy/recipe.html', context_dict)

def log_utterance(request):
    """Save the log of the user's utterance to the database"""
    if request.method == 'POST':
        session_id = request.POST['session_id']
        timestamp = request.POST['timestamp']
        recipe = request.POST['recipe']
        action = request.POST['action']
        confidence = request.POST['asrResults[0][confidence]']
        utterance = request.POST['asrResults[0][transcript]']
        current_step = request.POST['current_step']

        event = Event(session_id=session_id, timestamp=timestamp, recipe=recipe, confidence=confidence,
                      utterance=utterance, current_step=current_step, action=action)
        event.save()

    return HttpResponse()