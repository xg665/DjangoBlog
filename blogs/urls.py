from . import views
from django.urls import include, path

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('leetcode/',views.leetcode, name='leetcode'),
]
