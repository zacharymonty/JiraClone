from django.conf.urls import url
from django.contrib import admin

from jira import urls as jira_urls
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("", include(jira_urls)),
    url(r'^admin/', admin.site.urls)
]