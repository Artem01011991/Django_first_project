from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'chat'
urlpatterns = [
    path('', views.registration_page, name='registration_page'),
    path('userpage/<int:user_id>/', views.user_page, name='userpage'),
    path(
        'login/',
        LoginView.as_view(template_name='chat/log-in.html'),
        name='login',
         ),
]
