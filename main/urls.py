from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^(?P<username>[a-z]*)/$', views.profile, name='profile'),
]