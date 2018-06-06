# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_article.consts import PUBLISH_STATUS, DRAFT


class ArticleManager(models.Manager):
    def get_article(self, aid):
        return self.filter(id=aid).first()


class Article(models.Model):
    cover_image = models.ImageField(
        upload_to='media/article/%Y/%m',
        verbose_name=_('cover_image')
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_('title')
    )
    status = models.IntegerField(
        choices=PUBLISH_STATUS,
        verbose_name=_('status'),
        default=DRAFT
    )
    content = models.TextField(
        default='',
        verbose_name=_('content'),
        blank=True
    )
    desc = models.TextField(
        default='',
        verbose_name=_('desc'),
        blank=True
    )
    objects = ArticleManager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Article Management")

    def __unicode__(self):
        return self.title
