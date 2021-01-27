from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from user.views import register as register_views
from user.views import profile as profile_views
from django.contrib.auth import views as auth_views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.PostCreate.as_view(template_name='blogs/posts.html'), name='post'),
    path('posts/<int:pk>/', views.PostDetail.as_view(template_name='blogs/post_detail.html'),name='post-detail'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(template_name='blogs/posts.html'),name='post-update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(template_name='blogs/post_delete.html'),name='post-delete'),
    path('leetcode/',views.leetcode, name='leetcode'),
    path('register/', register_views, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('profile/<slug:slug>/',profile_views.as_view(),name='profile')

]
