from django.urls import re_path
from django.contrib import admin

from property import views

urlpatterns = [
    re_path(r'^$', views.show_flats),
    re_path(r'^search/$', views.show_flats),
    re_path(r'^admin/', admin.site.urls),
]
