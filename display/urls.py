from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^main/', views.main, name='main'),
    url(r'^$', views.index, name='index')
]
