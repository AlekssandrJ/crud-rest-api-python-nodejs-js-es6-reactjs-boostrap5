from django.conf.urls import url
from taskApp import views

urlpatterns = [
    url(r'^task$', views.taskApi),
    url(r'^task/([0-9]+)$',views.taskApi)
]