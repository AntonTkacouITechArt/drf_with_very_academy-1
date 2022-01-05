from django.urls import path

from blog.views import TemplateView1

urlpatterns = [
    path('', TemplateView1.as_view(), name='index')
]
