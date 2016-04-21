# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
                       url(r'^$', views.list_view, name="list_view"),
                       url(r'^(?P<student_id>\d+)/$',
                           views.detail, name='detail'),
                       url(r'^add/$', views.students_add, name='add'),
                       url(r'^edit/(?P<student_id>\d+)/$',
                           views.students_edit, name='edit'),
                       url(r'^remove/(?P<student_id>\d+)/$',
                           views.students_remove, name='remove'),
                       )
