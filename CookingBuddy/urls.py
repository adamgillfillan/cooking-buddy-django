__author__ = 'adam'
from django.conf.urls import patterns, url
from CookingBuddy import views

urlpatterns = patterns(
    '',
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^recipe/(?P<recipe>.+)$', views.recipe),
    url(r'^log_utterance', views.log_utterance, name='log_utterance')
)