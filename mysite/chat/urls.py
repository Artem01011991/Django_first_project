from django.urls import path
from . import views
from django.contrib.auth.views import login


app_name = 'chat'
urlpatterns = [
    path('', views.registration_page, name='registration_page'),
    path('userpage/', views.user_page, name='userpage'),
    path('login/', login, {'template_name': 'chat/log-in.html'}, name='login'),
]
