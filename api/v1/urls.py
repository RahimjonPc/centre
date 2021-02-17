from django.urls import path
from .users.views import LeaderView, TeachersListView, StudentListView, TeacherAccountView, StudentAccountView, TeacherCreateView, TeacherPasswordUpdateView, StudentCreateView, StudentUpdateView, StudentGroupListView, StudentGroupCreateView
from .events.views import EventsListView, EventsDetailView
from .cources.views import CoursesListView, CoursesDetail
from .marks.views import MarkDetailView, MarksListView

app_name = 'api_v1'

urlpatterns = [
    path('leader/list/', LeaderView.as_view(), name='leader'),
    path('teacher/list/', TeachersListView.as_view(), name='teacher_list'),
    path('student/list/', StudentListView.as_view(), name='student_list'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('student/group_list/', StudentGroupListView.as_view(), name='student_group_list'),
    path('student/group_create/', StudentGroupCreateView.as_view(), name='student_group_create'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/update/<int:pk>', TeacherPasswordUpdateView.as_view(), name='teacher_update'),
    path('teacher/password_update/', TeacherPasswordUpdateView.as_view(), name='teacher_password_update'),
    path('events/list/', EventsListView.as_view(), name='events_list'),
    path('cources/list/', CoursesListView.as_view(), name='course_list'),
    path('cources/detail/<int:pk>', CoursesDetail.as_view(), name='cources_detail'),
    path('teacher/accaunt/<int:pk>', TeacherAccountView.as_view(), name='teacher_accaunt'),
    path('student/accaunt/<int:pk>', StudentAccountView.as_view(), name='student_accaunt'),
    path('mark/detail/<int:pk>', MarkDetailView.as_view(), name='mark_detail'),
    path('mark/list/', MarksListView.as_view(), name='mark_list'),
    path('event/detail/<int:pk>', EventsDetailView.as_view(), name='event_detail'),
]