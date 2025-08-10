from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'full_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class UserProfileListSerializer(serializers.ModelSerializer):
    # gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'full_name']


class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    created_by = UserProfileListSerializer()
    category = CategorySerializer(many=True, read_only=True)
    level_display = serializers.CharField(source='get_level_display', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'level_display',
                  'price', 'video', 'created_at', 'updated_at',
                  'created_by', 'category']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'content', 'course']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentListSerializer(serializers.ModelSerializer):
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    assignment_type_display = serializers.CharField(source='get_assignment_type_display', read_only=True)
    due_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    lesson = LessonListSerializer()

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'level_display', 'due_date',
                  'assignment_type_display', 'submitted_by', 'is_active', 'lesson']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamListSerializer(serializers.ModelSerializer):
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    due_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'level_display',
                  'due_date', 'passing_score', 'is_active']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'true_answer']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_courses = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_courses']


class CourseDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    created_by = UserProfileListSerializer()
    category = CategorySerializer(many=True, read_only=True)
    course_lessons = LessonListSerializer(many=True, read_only=True)
    level_display = serializers.CharField(source='get_level_display', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'level_display',
                  'price', 'video', 'created_at', 'updated_at',
                  'created_by', 'category', 'course_lessons']


class ExamDetailSerializer(serializers.ModelSerializer):
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    due_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    exam_questions = QuestionListSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'passing_score', 'is_active',
                  'exam_questions', 'due_date', 'level_display']
