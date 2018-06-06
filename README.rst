django-article
^^^^^^^^
Note: This project is still under-development.

Author: 234082230@qq.com

Introduction
---------
- Added Article model
- Added ArticleAdmin, ArticleManager
- Added Article list, detail api
- Added Article list, detail view

settings.py
---------
 ::

    INSTALLED_APPS = [
        ...
        'django_article',
        ...
    ]

    TEMPLATES = [
        {
            ...

            'DIRS': ['templates'],

            ...
        }
    ]

urls.py
---------
 ::

    from django.conf import settings
    from django.conf.urls import url, include
    from django.conf.urls.static import static
    from django.contrib import admin
    from django.views.i18n import JavaScriptCatalog
    from django_article.views.user import UserLoginView, UserLogoutView, UserRegisterView

    urlpatterns = [
        url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),

        url(r'^admin/', admin.site.urls),

        url(r'^article/list/', ArticleListView.as_view()),
        url(r'^article/(?P<aid>[0-9]+)/$', ArticleDetailView.as_view()),

        url(r'^api/article/', include('django_article.urls', namespace='django-article')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



