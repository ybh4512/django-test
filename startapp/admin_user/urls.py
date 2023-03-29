from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(\d+)/edit/$', views.edit, name='edit'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(\d+)/update/$', views.update, name='update'),
    url(r'^(\d+)/delete/$', views.delete, name='delete'),

    url(r'^time/$', views.today_is, name='time'),
    url(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile')
]
