# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import re
import sys
import time
import uuid
from datetime import datetime
from random import random

from django.conf import settings
from django.http.response import JsonResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from django_article.views.base import api_common
from django_article.models import Article


class APIArticleListView(View):
    def post(self, request):
        articles = Article.objects.all()
        article_data = []
        for article in articles:
            article_data.append({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'desc': article.desc,
                'cover_image': article.cover_image.url,
            })
        response = api_common({
            'articles': article_data
        })
        return JsonResponse(response)


class APIArticleDetailView(View):
    def post(self, request):
        aid = request.POST.get('aid', '')
        article = Article.objects.get_article(aid=aid)

        article_data = {
            'id': article.id,
            'cover_image': article.cover_image.url,
            'title': article.title,
            'status': article.status,
            'content': article.content,
            'desc': article.desc,
        }

        prev_aid = int(aid) - 1
        prev_article = json.dumps(None)
        if prev_aid > 0:
            article = Article.objects.get_article(prev_aid)
            if article:
                prev_article = json.dumps({'id': article.id, 'title': article.title})

        next_aid = int(aid) + 1
        next_article = json.dumps(None)
        if next_aid > 0:
            article = Article.objects.get_article(next_aid)
            if article:
                next_article = json.dumps({'id': article.id, 'title': article.title})

        context = {
            'article': article_data,
            'prev_article': prev_article,
            'next_article': next_article,
        }
        response = api_common(context)
        return JsonResponse(response)
