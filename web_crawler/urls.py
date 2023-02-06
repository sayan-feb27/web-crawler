from django.contrib import admin
from django.urls import path

from .views import HomePage, CrawlerView, NestedView


urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('nested/', NestedView.as_view(), name="nested"),
    path('crawl', CrawlerView.as_view(), name="crawl"),
    path('admin/', admin.site.urls),
]
