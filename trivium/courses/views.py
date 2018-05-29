from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Course, Lesson, Question, Answer, UserCourse, UserLesson
from ..users.permissions import IsUserOrReadOnly, IsStaff
from .serializers import CourseSerializer, LessonSerializer, LessonDetailSerializer


class CourseAdminViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsStaff,)


class CourseViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if not self.request.user.is_staff \
                and not self.request.user.is_superuser:
            user_courses = UserCourse.objects.filter(user=self.request.user)
            return Course.objects.filter(id__in=user_courses)
        return Course.objects.all()


class LessonAdminViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsStaff,)


class LessonViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if not self.request.user.is_staff \
                and not self.request.user.is_superuser:
            user_lessons = UserLesson.objects.filter(user=self.request.user)
            return Lesson.objects.filter(id__in=user_lessons)
        return Lesson.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LessonDetailSerializer
        return LessonSerializer

