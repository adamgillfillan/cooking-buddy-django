from django.http import HttpResponse
from django.shortcuts import render
from CookingBuddy.models import Event
from CookingBuddy.decorators import require_user_name


def new_user(request):
    return render(request, 'cooking_buddy/new_user.html')

@require_user_name
def index(request):
    context_dict = {}
    return render(request, 'cooking_buddy/index.html', context_dict)

@require_user_name
def about(request):
    context_dict = {}
    return render(request, 'cooking_buddy/about.html', context_dict)

@require_user_name
def recipe(request, recipe):
    context_dict = {"recipe": recipe}
    return render(request, 'cooking_buddy/recipe.html', context_dict)


def log_utterance(request):
    """Save the log of the user's utterance to the database"""
    if request.method == 'POST':
        name = request.COOKIES.get('name')
        session_id = request.POST['session_id']
        timestamp = request.POST['timestamp']
        recipe = request.POST['recipe']
        action = request.POST['action']
        confidence = request.POST['asrResults[0][confidence]']
        utterance = request.POST['asrResults[0][transcript]']
        current_step = request.POST['current_step']

        event = Event(name=name, session_id=session_id, timestamp=timestamp, recipe=recipe,
                      action=action, confidence=confidence, utterance=utterance, current_step=current_step)
        event.save()

    return HttpResponse()