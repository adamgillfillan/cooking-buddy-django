from django.shortcuts import render
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