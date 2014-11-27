__author__ = 'adam'
from django.conf.urls import patterns, url
from CookingBuddy import views

urlpatterns = patterns(
    '',
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^salisbury_steak', views.salisbury_steak, name='salisbury_steak'),
    url(r'^cinnamon_rock_candy', views.cinnamon_rock_candy, name='cinnamon_rock_candy'),
    url(r'^green_bean_casserole', views.green_bean_casserole, name='green_bean_casserole'),
    url(r'^pumpkin_french_toast', views.pumpkin_french_toast, name='pumpkin_french_toast'),
    url(r'^spinach_and_bacon_quiche', views.spinach_and_bacon_quiche, name='spinach_and_bacon_quiche'),
    url(r'^log_utterance', views.log_utterance, name='log_utterance'),
)