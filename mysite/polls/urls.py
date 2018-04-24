from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
