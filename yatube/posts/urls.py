from django.urls import path

from .views import group_posts, index

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('group/<slug:slug>/', group_posts, name='group_list')
]
