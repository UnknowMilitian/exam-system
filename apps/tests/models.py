from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Subject Name")
    order = models.PositiveIntegerField(verbose_name="Order", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        ordering = ["order", "created_at"]
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name[:50] + "..." if len(self.name) > 50 else self.name


class Test(models.Model):
    question_text = models.TextField(verbose_name="Question")
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT, verbose_name="Subject"
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Test"
        verbose_name_plural = "Tests"

    def __str__(self):
        return (
            self.question_text[:50] + "..."
            if len(self.question_text) > 50
            else self.question_text
        )


class TestQuestion(models.Model):
    answer_text = models.TextField(verbose_name="Answer")
    is_correct = models.BooleanField(verbose_name="Is Correct", default=False)
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="questions", verbose_name="Test"
    )

    class Meta:
        verbose_name = "Test Question"
        verbose_name_plural = "Test Questions"

    def clean(self):
        if TestQuestion.objects.filter(test=self.test, is_correct=True).exists():
            raise ValidationError(
                {"is_correct": "Only one correct answer per test question is allowed."}
            )

    def __str__(self):
        return (
            self.answer_text[:50] + "..."
            if len(self.answer_text) > 50
            else self.answer_text
        )
