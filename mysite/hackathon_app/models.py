from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

LEVEL_CHOICES = (
    ('beginner', _('Beginner')),
    ('medium', _('Medium')),
    ('advanced', _('Advanced')),
)

TYPE_CHOICES = (
    ('text', _('Text')),
    ('test', _('Test')),
    ('file', _('File')),

)

ROLE_CHOICES = (
    ('teacher', 'teacher'),
    ('student', 'student'),
)


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True, blank=True, region='KG')
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.username}'


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    description = models.TextField()
    category = ManyToManyField(Category, related_name='category_courses')
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    price = models.PositiveSmallIntegerField()
    video = models.FileField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course_name}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_lessons')
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.TextField()
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    due_date = models.DateTimeField()
    assignment_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    submitted_by = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.TextField()
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    due_date = models.DateTimeField()
    passing_score = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(10), MaxValueValidator(100)
    ])
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_questions')
    question = models.TextField()
    true_answer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.exam}'


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.URLField()

    def __str__(self):
        return f'{self.student} > {self.course}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} > {self.course}'
