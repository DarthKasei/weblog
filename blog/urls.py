__author__ = 'gcampbell01'
from django.conf import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name='post_list'),
]