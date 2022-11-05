from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('', views.home_view, name='home'),
]