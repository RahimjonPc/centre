from django.urls import path, include
from .views import MarkDetailView, MarksListView

urlpatterns = [
    path('mark/list/', MarksListView.as_view(), name='mark_list'),
    path('mark/detail/<int:pk>', MarkDetailView.as_view(), name='mark_detail'),
]