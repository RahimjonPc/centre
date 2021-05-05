from django.urls import path, include
from .views import CoursesListView, CoursesUpdate, CourseDelete, CourseCreate

app_name = 'course'

urlpatterns = [
    path('cource/list/', CoursesListView.as_view(), name='course_list'),
    path('cource/create/', CourseCreate.as_view(), name='cources_create'),
    path('cource/update/<int:pk>', CoursesUpdate.as_view(), name='cources_update'),
    path('course/delete/<int:pk>', CourseDelete.as_view(), name='course_delete'),
]
