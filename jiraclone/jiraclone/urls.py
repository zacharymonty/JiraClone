from django.conf.urls import url
from django.contrib import admin


from jira import urls
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("", include(urls)),
    url(r'^admin/', admin.site.urls)
]