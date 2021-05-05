from django import forms
from .models import Courses

class CourceCreateForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'