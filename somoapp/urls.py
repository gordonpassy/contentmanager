from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Subjects, name='Subjects'),
    #subject/id
    url(r'^subject(\d+)',views.Chapter,name ='Chapter'),
    #topics
    #subject/chapter_id/topic_id

    # url(r'^subject/(\d+)/(P?<topic_id>)',views.Chapter,name ='topics'),

    # url(r'subject/(?P<id>[0-9]+)/topic/$', views.Chapter, name='topics'),

    url(r'^subject/(\d+)/$',views.Topics,name='topics'),

    # url(r'^subject/(?P<pk>\d+)/$', views.Topics, name='topics'),


    #subject/chapter_id/topic_id/pages_id
    url(r'^subject/(\d+)',views.Chapter,name ='pages'),

    ]
