from rest_framework.urls import path
from .views import *


urlpatterns = [
    # user
    path('user/', UserProfileAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('user/<int:pk>/edit', UserProfileEditAPIView.as_view(), name='user_edit'),

    # category
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    # course
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('course/<int:pk>/edit/', CourseEditAPIView.as_view(), name='course_edit'),

    # lesson
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/edit/', LessonEditAPIView.as_view(), name='lesson_edit'),

    # assignment
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment_list'),
    path('assignment/create/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('assignment/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment_detail'),
    path('assignment/<int:pk>/edit/', AssignmentEditAPIView.as_view(), name='assignment_edit'),

    # exam
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('exam/<int:pk>/edit/', ExamEditAPIView.as_view(), name='exam_edit'),

    # question
    path('question/create/', QuestionCreateAPIView.as_view(), name='question_create'),
    path('question/<int:pk>/edit/', QuestionEditAPIView.as_view(), name='question_edit'),

    # certificate
    path('certificate/create/', CertificateCreateAPIView.as_view(), name='certificate_create'),

    # review
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
]

