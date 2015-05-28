__author__ = 'Ronald'
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^base$', index.as_view(), name='base'),
    url(r'^$', 'django.contrib.auth.views.login',
        {'template_name':'inicio/login.html'}, name='login'),
    url(r'^cerrar$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),

]
