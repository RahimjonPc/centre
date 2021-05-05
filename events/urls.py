from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('/event/list', views.EventsListView.as_view(), name='event_list'),
    path('/event/create', views.CreateEventView, name='event_create'),
    path('/event/update/<int:pk>', views.UpdateEventView, name='event_update'),
    path('/event/delete/<int:pk>', views.EventDeleteView, name='event_delete'),
]