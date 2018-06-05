# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

DRAFT = -2
PENDING_REVIEW = 0
PUBLISH = 1
UNPUBLISH = -1
DELETED = -3
PUBLISH_STATUS = (
    (DRAFT, _('draft')),
    (PENDING_REVIEW, _('pending')),
    (PUBLISH, _('published')),
    (UNPUBLISH, _('unpublished')),
    (DELETED, _('deleted')),
)
