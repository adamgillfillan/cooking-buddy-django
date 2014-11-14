from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.


def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('cooking_buddy/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('cooking_buddy/about.html', context_dict, context)


def salisbury_steak(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('cooking_buddy/salisbury_steak.html', context_dict, context)