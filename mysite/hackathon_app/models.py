from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


LEVEL_CHOICES = (
    ('beginner', 'beginner'),
    ('medium', 'medium'),
    ('advanced', 'advanced'),
)

TYPE_CHOICES = (
    ('text', 'text'),
    ('test', 'test'),
    ('file', 'file'),
)


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True, blank=True, region='KG')


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    price = models.PositiveSmallIntegerField()
    video = models.FileField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField()


class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.TextField()
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    due_date = models.DateTimeField()
    assignment_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    submitted_by = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)


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


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()
    true_answer = models.BooleanField(default=False)


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.URLField()


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    comment = models.TextField()
