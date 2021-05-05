from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'

urlpatterns = [
    path('/login', views.AuthericationView.as_view(), name='login'),
    path('/logout', views.UserLogoutView.as_view(), name='logout'),

    path('/myprofile', views.myprofile, name='myprofile'),
    path('/question', views.question, name='question'),

    path('/student/register', views.StudentRegisterView.as_view(), name='student_register'),
    path('/student/list', views.StudentListView.as_view(), name='student_list'),
    path('/student/profile', views.StudentProfile, name='student_profile'),
    path('/student/detail/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
    path('/student/update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update'),
    path('/student/delete/<int:pk>', views.StudentDeleteView, name='student_delete'),
    
    path('/leader/profile', views.LeaderProfile, name='leader_profile'),
    path('/my/users', views.UsersListView.as_view(), name='my_users'),
    path('/user/create', views.UserCreateView.as_view(), name='user_create'),
    path('/user/detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('/user/update/<int:pk>', views.UserUpdadeView.as_view(), name='user_update'),
    path('/user/delete/<int:pk>', views.UserDeleteView, name='user_delete'),

    # path('/teacher/register', views.TeacherRegisterView.as_view(), name='teacher_register'),
    path('/teacher/register', views.TeacherRegisterView, name='teacher_register'),
    path('/teacher/list', views.TeacherListView.as_view(), name='teacher_list'),
    path('/teacher/profile', views.TeacherProfile, name='teacher_profile'),
    path('/teacher/detail/<int:pk>', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('/teacher/update/<int:pk>', views.TeacherUpdateView, name='teacher_update'),
    path('/teacher/delete/<int:pk>', views.TeacherDeleteView, name='teacher_delete'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)