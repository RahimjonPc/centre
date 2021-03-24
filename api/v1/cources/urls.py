from django.urls import path, include
from .views import CoursesListView, CoursesDetail

urlpatterns = [
    path('cource/list/', CoursesListView.as_view(), name='course_list'),
    path('cource/detail/<int:pk>', CoursesDetail.as_view(), name='cources_detail'),
]
