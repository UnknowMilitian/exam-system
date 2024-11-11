from django.db import models


# Create your models here.
class Exam(models.Model):
    title = models.CharField(max_length=255, verbose_name="Exam Title")
    pass_percentage = models.PositiveIntegerField(verbose_name="Pass Percentage")
    start_time = models.DateTimeField(verbose_name="Start Time")
    end_time = models.DateTimeField(verbose_name="End Time")
    test_count = models.PositiveIntegerField(verbose_name="Number of Tests")
    subject = models.ForeignKey(
        "tests.Subject", on_delete=models.CASCADE, verbose_name="Subject"
    )
    users = models.ManyToManyField(
        "users.User", through="ExamStudents", verbose_name="Students"
    )

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"


class ExamTest(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="Exam")
    test = models.ForeignKey(
        "tests.Test", on_delete=models.CASCADE, verbose_name="Test"
    )
    order = models.PositiveIntegerField(verbose_name="Order", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        ordering = ["order", "created_at"]
        verbose_name = "Exam Test"
        verbose_name_plural = "Exam Tests"


class ExamStudents(models.Model):
    class StatusType(models.TextChoices):
        NOT_PASSED = ("Not Passed", "Not Passed")
        PASSED = ("Passed", "Passed")

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="Exam")
    student = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="Student"
    )
    status = models.CharField("Status", max_length=16, default=StatusType.NOT_PASSED)
    total_score = models.FloatField(verbose_name="Total Score", default=0)

    class Meta:
        verbose_name = "Exam Student"
        verbose_name_plural = "Exam Students"


class StudentExamTestAnswer(models.Model):
    student = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="Student"
    )
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, verbose_name="Exam")
    test = models.ForeignKey(
        "tests.Test", on_delete=models.PROTECT, verbose_name="Test"
    )
    selected_answer = models.ForeignKey(
        "tests.TestQuestion",
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Selected Answer",
    )
    is_correct_answer = models.BooleanField(
        verbose_name="Is Correct Answer", null=True, blank=True
    )

    class Meta:
        verbose_name = "Student Exam Test Answer"
        verbose_name_plural = "Student Exam Test Answers"
