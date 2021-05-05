from django import forms
from django.forms import TextInput, Textarea, DateTimeInput, Select, PasswordInput
from .models import LeaderProfile, Teacher, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class AuthUserForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class TeacherForm(forms.ModelForm):
    username = forms.CharField(max_length=100) 
    password = forms.CharField() 
    class Meta:
        model = Teacher
        fields = ['username', 'password', 'cources','bio','experience','sex','birthday','phone']

    
    
        # widgets = {
        #     "cources": Select(attrs={
        #         'class': 'form-control',
        #     }),
        #     "bio": Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Bio'
        #     }),
        #     "experience": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Experience'
        #     }),
        #     "sex": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Sex'
        #     }),
        #     "birthday": DateTimeInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Birthday'
        #     }),
        #     "phone": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Phone'
        #     }),
        # }


class StudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Student
        fields = ['user', 'sex','birthday','phone']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user