from django.shortcuts import render, redirect
from .models import Events
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms  import EventForm
from django.urls import reverse_lazy, reverse
from users.models import Teacher, StudentGroup
from cources.models import Courses


class EventsListView(ListView):
    model = Events
    template_name = 'events/event_list.html'
    context_object_name = 'events'

# class EventCreateView(CreateView):
#     model = Events
#     template_name = 'events/event_create.html'
#     form_class = EventForm
#     success_url = reverse_lazy('events:event_list')

def CreateEventView(request):
    teachers = Teacher.objects.all()
    courses = Courses.objects.all()
    studentgroup = StudentGroup.objects.all()

    context = {
        'teachers':teachers,
        'courses':courses,
        'studentgroups':studentgroup,
    }
    return render(request, 'events/event_create.html', context)


def UpdateEventView(request, pk):
    teachers = Teacher.objects.all()
    courses = Courses.objects.all()
    studentgroup = StudentGroup.objects.all()

    context = {
        'teachers':teachers,
        'courses':courses,
        'studentgroups':studentgroup,
    }
    return render(request, 'events/event_update.html', context)

# class EventUpdateView(UpdateView):
#     model = Events
#     template_name = 'events/event_update.html'
#     form_class = EventForm
#     success_url = reverse_lazy('events:event_list')


def EventDeleteView(request, pk):
    event = Events.objects.filter(pk=pk)
    event.delete()
    return redirect(reverse('events:event_list'))