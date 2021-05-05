from django.shortcuts import render, redirect
from .models import Courses
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import CourceCreateForm
from django.urls import reverse_lazy
from django.urls import reverse

class CourceListView(ListView):
    model = Courses
    template_name = 'cources/cource_list.html'
    context_object_name = 'cources'



class CourceCreateView(CreateView):
    template_name = 'cources/create_cource.html'
    form_class = CourceCreateForm
    success_url = reverse_lazy('cources:cource_list')



class CourceUpdateView(UpdateView):
    model = Courses
    form_class = CourceCreateForm
    template_name = 'cources/course_update.html'
    success_url = reverse_lazy('cources:cource_list')


def DeleteView(request, pk):
    cource = Courses.objects.filter(pk=pk)
    cource.delete()

    return redirect(reverse('cources:cource_list'))

