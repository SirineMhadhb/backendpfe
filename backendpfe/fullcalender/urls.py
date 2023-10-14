from django.urls import include, re_path

from . import views

app_name = "fullcalender"
urlpatterns = [
re_path('^calendar', views.calendar, name='calendar'),
re_path('^add_event$', views.add_event, name='add_event'),
re_path('^update$', views.update, name='update'),
re_path('^remove', views.remove, name='remove'),]