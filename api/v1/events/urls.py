from django.urls import path, include
from .views import EventsListView, EventsDetailView

urlpatterns = [
    path('events/list/', EventsListView.as_view(), name='events_list'),
    path('event/detail/<int:pk>', EventsDetailView.as_view(), name='event_detail'),
]