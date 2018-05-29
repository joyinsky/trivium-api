from rest_framework import serializers
from .models import Course, Lesson, Question, Answer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'score_to_pass')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class CourseDetailSerializer(CourseSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta(CourseSerializer.Meta):
        pass


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


class QuestionDetailSerializer(QuestionSerializer):
    answers = AnswerSerializer(many=True)

    class Meta(QuestionSerializer.Meta):
        pass


class LessonDetailSerializer(LessonSerializer):
    questions = QuestionDetailSerializer(many=True, read_only=True)

    class Meta(LessonSerializer.Meta):
        pass
