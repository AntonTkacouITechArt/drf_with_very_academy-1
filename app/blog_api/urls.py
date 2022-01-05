from django.urls import path

from blog_api.views import PostDetailAPI, PostListAPI

app_name = 'blog_api/v1/'

urlpatterns = [
    path('', PostListAPI.as_view(), name='list_post'),
    path('<int:pk>', PostDetailAPI.as_view(), name='detail_post'),

]
