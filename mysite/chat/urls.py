from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.registration_page, name='registration_page'),
    url(r'^userpage/$', views.user_page, name='userpage'),
    url(r'login/$', login, {'template_name': 'chat/log-in.html'}, name='login'),
]
