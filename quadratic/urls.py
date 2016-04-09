from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
                       # url(r'^$', views.quadratic_results, name='quadratic_results'),
                       url(r'^results/$', views.quadratic_results, name='quadratic_results'),
                       # url(r'^results/(?P<question_id>\d+)/$', views.results, name='results'),
                       )
