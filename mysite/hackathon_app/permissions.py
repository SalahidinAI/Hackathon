from rest_framework import permissions


class UserEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsLessonOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.course.created_by == request.user


class IsAssignmentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.lesson.course.created_by == request.user


class IsExamOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.course.created_by == request.user


class IsQuestionOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.exam.course.created_by == request.user


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'teacher'


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'

