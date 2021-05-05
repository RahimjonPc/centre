from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import AuthUserForm
from django.urls import reverse_lazy



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
