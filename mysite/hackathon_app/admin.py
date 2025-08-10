from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class GeneralMedia:
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Course)
class CourseAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Lesson)
class LessonAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Assignment)
class AssignmentAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Exam)
class ExamAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Question)
class QuestionAdmin(TranslationAdmin, GeneralMedia):
    pass


admin.site.register(UserProfile)
admin.site.register(Certificate)
admin.site.register(Review)

