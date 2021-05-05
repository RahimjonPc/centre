from rest_framework import generics
from cources.models import Courses
from .serializers import CoursesListSerializer
from users.models import Teacher
from rest_framework.permissions import AllowAny
# from events.models import Events

class CoursesListView(generics.ListAPIView):
    model = Courses
    serializer_class = CoursesListSerializer

    def get_queryset(self):
        cources = Courses.objects.all()
        if self.request.GET.get('teacher'):
            teacher_id = self.request.GET.get('teacher')
            return Courses.objects.filter(teacher__id=teacher_id)
        else:
            return Courses.objects.all()

class CourseCreate(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesListSerializer
    permission_classes = [AllowAny]
        
class CoursesUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesListSerializer
    permission_classes = [AllowAny]


class CourseDelete(generics.DestroyAPIView):
    serializer_class = CoursesListSerializer
    permission_classes = [AllowAny]