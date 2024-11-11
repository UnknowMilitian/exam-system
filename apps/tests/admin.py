from django.contrib import admin

from apps.tests.models import Subject, Test, TestQuestion


# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    pass
