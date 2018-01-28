from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^api/1.0/cron/add$',       views.cron_add,       name='cron_add'),
    url(r'^api/1.0/cron/del$',       views.cron_del,       name='cron_del'),
    url(r'^api/1.0/cron/pause$',     views.cron_pause,     name='cron_edit'),
    url(r'^api/1.0/cron/resume$',    views.cron_resume,    name='cron_resume'),
    url(r'^api/1.0/cron/list$',      views.cron_list,      name='cron_list'),

]