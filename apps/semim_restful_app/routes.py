from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows$',views.allShows),
    url(r'^shows/new$',views.create),
    url(r'^shows/(?P<id>\d+)/edit$',views.edit),
    url(r'^shows/(?P<id>\d+)$',views.read),
    url(r'^add_show',views.add_show),
    url(r'^edit_show/(?P<id>\d+)$',views.edit_show),
    url(r'^delete/(?P<id>\d+)$',views.delete),
    url(r'^$',views.allShows),

]