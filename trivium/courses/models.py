from django.db import models
from django.conf import settings
from ordered_model.models import OrderedModel


class Course(OrderedModel):
    name = models.CharField(max_length=100)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name or ''


class Lesson(OrderedModel):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score_to_pass = models.IntegerField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name or ''


class Question(models.Model):
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    all_correct = models.BooleanField(default=False)
    score = models.IntegerField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField()


class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)
    is_correct = models.BooleanField()
    score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)


class UserLesson(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.IntegerField()
    approved = models.BooleanField()


class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    approved = models.BooleanField()
