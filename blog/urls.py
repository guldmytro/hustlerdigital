from django.urls import path
from blog import views

app_name = 'news'

urlpatterns = [
    path('<int:pk>/comment/', views.blog_comment, name='comment'),
    path('<int:pk>/add-like/', views.add_like, name='add_like'),
    path('<int:pk>/remove-like/', views.delete_like, name='delete_like'),
    path('<int:pk>/', views.blog_detail, name='detail'),
    path('', views.blog_list, name='list')
]