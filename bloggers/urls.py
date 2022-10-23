from django.urls import path
from bloggers import views

app_name = 'bloggers'

urlpatterns = [
    path('', views.bloggers_list, name='list')
]