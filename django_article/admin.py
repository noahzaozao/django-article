# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils.translation import ugettext_lazy as _

from django_article.models import Article


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    def make_publish(self, request, queryset):
        queryset.update(publish_type=1, status=1)

    make_publish.short_description = _("publish")

    def make_unpublish(self, request, queryset):
        queryset.update(publish_type=0, status=0)

    make_unpublish.short_description = _("unpublish")

    search_fields = ['title']
    list_display = ('title', 'desc')
    list_filter = ('status',)
    actions = ['make_publish', 'make_unpublish']
