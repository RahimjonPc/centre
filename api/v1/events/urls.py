from django.urls import path, include
from .views import EventsListView, EventsUpdateView, EventCreateView

app_name = 'event'

urlpatterns = [
    path('event/list/', EventsListView.as_view(), name='events_list'),
    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/update/<int:pk>', EventsUpdateView.as_view(), name='event_update'),
]