from django.urls import path, include
from .views import LeaderView, TeachersListView, TeacherUpdateView, StudentListView, TeacherCreateView, TeacherPasswordUpdateView, StudentCreateView, StudentUpdateView, StudentGroupListView, StudentGroupCreateView, LoginView, MyTokenObtainPairView

app_name = 'user'

urlpatterns = [
    path('leader/list/', LeaderView.as_view(), name='leader'),

    path('student/list/', StudentListView.as_view(), name='student_list'),
    path('student/create', StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('student/group_list/', StudentGroupListView.as_view(), name='student_group_list'),
    path('student/group_create/', StudentGroupCreateView.as_view(), name='student_group_create'),

    path('teacher/list/', TeachersListView.as_view(), name='teacher_list'),
    path('teacher/create', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/update/password/<int:pk>', TeacherPasswordUpdateView.as_view(), name='teacher_update'),
    path('teacher/update/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    # path('teacher/password_update/', TeacherPasswordUpdateView.as_view(), name='teacher_password_update'),

    path('login/', LoginView.as_view(), name='custom_login'),
    path('customjwt/', MyTokenObtainPairView.as_view(), name='customjwt'),
]   