from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^today/$', views.news_today, name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_day_news, name='Archived news'),
    url(r'^search/$', views.search_results, name='search'),
    url(r'^article/(\d+)', views.article, name='article'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
