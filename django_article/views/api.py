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
                'title': article.title,
                'content': article.content,
                'desc': article.desc,
            })
        response = api_common({
            'article_data': article_data
        })
        return JsonResponse(response)


class APIArticleDetailView(View):
    def post(self, request):
        response = api_common({})
        return JsonResponse(response)
