from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from .forms import AuthUserForm, TeacherForm, StudentForm, UserCreateForm
from .models import LeaderProfile, Teacher, Student
from cources.models import Courses


class AuthericationView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthUserForm    
    
    def get_success_url(self):
        if hasattr(self.request.user, 'teacher'):
            success_url = reverse_lazy('users:teacher_profile')
        elif hasattr(self.request.user, 'student'):
            success_url = reverse_lazy('users:student_profile')
        elif hasattr(self.request.user, 'leader'):
            success_url = reverse_lazy('users:leader_profile')

        return success_url

    

# class RegistrationView(CreateView):
#     template_name = 'users/registration.html'
#     form_class = RegUserForm
#     success_url = reverse_lazy('users:question')
    
#     def form_valid(self, form):
#         form_valid = super().form_valid(form)
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         auth_user = authenticate(username=username,password=password)
#         login(self.request, auth_user)
#         return form_valid

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


def myprofile(request):
    return render(request, 'users/myprofile.html')


def question(request):
    return render(request, 'users/question.html')


# class TeacherRegisterView(TemplateView):
#     template_name = 'users/teacher_register.html'

def TeacherRegisterView(request):
    courses = Courses.objects.all()
    context = {
        'courses':courses,
    }
    return render(request, 'users/teacher_register.html',context)

    

class StudentRegisterView(CreateView):
    template_name = 'users/student_register.html'
    form_class = StudentForm
    success_url = reverse_lazy('users:leader_profile')


def StudentProfile(request):
    return render(request, 'users/student_profile.html')


def TeacherProfile(request):
    return render(request, 'users/teacher_profile.html')


def LeaderProfile(request):
    return render(request, 'users/leader_profile.html')
    

class UsersListView(ListView):
    model = User
    template_name = 'users/my_users.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('users:my_users')


class UserDetailView(DeleteView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'users'


class UserUpdadeView(UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:my_users')


def UserDeleteView(request, pk):
    user = User.objects.filter(pk=pk)
    user.delete()
    return redirect(reverse('users:my_users'))


class TeacherListView(ListView):
    model = Teacher
    template_name = 'users/teacher_list.html'
    context_object_name = 'teachers'


class TeacherDetailView(DeleteView):
    model = Teacher
    template_name = 'users/teacher_detail.html'
    context_object_name = 'teachers'
    


# class TeacherUpdateView(UpdateView):
#     model = Teacher
#     form_class = TeacherForm
#     template_name = 'users/teacher_update.html'
#     success_url = reverse_lazy('users:teacher_list')

def TeacherUpdateView(request, pk):
    courses = Courses.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'users/teacher_update.html', context)


def TeacherDeleteView(request, pk):
    teacher = Teacher.objects.filter(pk=pk)
    teacher.delete()
    return redirect(reverse('users:teacher_list'))


class StudentListView(ListView):
    model = Student
    template_name = 'users/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DeleteView):
    model = Student
    template_name = 'users/student_detail.html'
    context_object_name = 'students'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student_update.html'
    success_url = reverse_lazy('users:student_list')


def StudentDeleteView(request, pk):
    student = Student.objects.filter(pk=pk)
    student.delete()
    return redirect(reverse('users:student_list'))
