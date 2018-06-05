"""mud7mv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from django_article.views import APIArticleListView, APIArticleDetailView


app_name = 'django-article'
urlpatterns = [

    url(r'^article/(?P<wid>[0-9]+)$', APIArticleDetailView.as_view()),
    url(r'^article/$', APIArticleListView.as_view()),

]
