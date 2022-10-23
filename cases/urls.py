from django.urls import path
from . import views as cases_views

app_name = 'cases'

urlpatterns = [
    path('', cases_views.cases_list, name='list')
]