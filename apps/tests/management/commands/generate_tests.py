import random
from django.core.management.base import BaseCommand

from apps.tests.models import Subject, Test, TestQuestion


class Command(BaseCommand):
    help = "Create a new subject and tests"

    def handle(self, *args, **kwargs):
        subjects = self.generate_subjects()
        tests = self.generate_tests(subjects)
        self.generate_test_questions(tests)

        self.stdout.write(self.style.SUCCESS(f"Subject, Test, Options  created"))

    def generate_subjects(self):
        subjects = ["Matematika", "Fizika", "Geografiya"]

        subjects_objs = []
        for subject in subjects:
            subject, _ = Subject.objects.get_or_create(
                name=subject, defaults={"order": random.randint(1, 10)}
            )
            subjects_objs.append(subject)

        return subjects_objs

    def generate_tests(self, subjects_objs):
        tests_objs = []
        for subject in subjects_objs:
            for i in range(100):
                test, _ = Test.objects.get_or_create(
                    question_text=f"Test {i + 1}", subject=subject
                )
                tests_objs.append(test)

        return tests_objs

    def generate_test_questions(self, tests_objs):
        for test in tests_objs:
            is_correct = False
            test_question_count = random.randint(3, 6)
            is_correct_answer_index = random.randint(1, test_question_count + 1)

            for i in range(test_question_count):
                if i + 1 == is_correct_answer_index:
                    is_correct = True
                test_question, _ = TestQuestion.objects.get_or_create(
                    answer_text=f"Test question {i + 1}",
                    is_correct=is_correct,
                    test=test,
                )
