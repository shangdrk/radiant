from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.sign_up, name='sign_up'),
    url(r'^signin/', views.sign_in, name='sign_in',),
    url(r'^user/(?P<username>)', views.temp, name='temp'),
]