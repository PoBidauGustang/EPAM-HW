import datetime

from application.models import Homework
from django.test import TestCase


class HomeworkTestCase(TestCase):
    def setUp(self):
        Homework.objects.create(
            text="Learn 1OOP", created=datetime.datetime.now(), deadline=5, teacher_id=1
        )

    def test_homework_text(self):
        data = Homework.objects.get(deadline=5)
        self.assertEqual(data.text, "Learn 1OOP")
