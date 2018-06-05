# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.template import loader
from django.views.generic import View


class ArticleListView(View):
    def get(self, request):
        template = loader.get_template('django_article/article/article_list.html')
        return HttpResponse(template.render({}, request))


class ArticleDetailView(View):
    def get(self, request):
        template = loader.get_template('django_article/article/article_detail.html')
        return HttpResponse(template.render({}, request))
