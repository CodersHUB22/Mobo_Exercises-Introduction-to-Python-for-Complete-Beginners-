from django.test import TestCase

from .models import Todo


class TodoTest(TestCase):

    def setUp(self):
        self.timestamp = date.today()
        self.task = Task(user=self.user,
                         description='description',
                         due=self.timestamp + timedelta(days=1))
        self.task.save()

    def tearDown(self):
        self.user.delete()

    def test_read_task(self):
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.description, 'description')
        self.assertEqual(self.task.due, self.timestamp + timedelta(days=1))

    def test_update_task_description(self):
        self.task.description = 'new description'
        self.task.save()
        self.assertEqual(self.task.description, 'new description')

    def test_update_task_due(self):
        self.task.due = self.timestamp + timedelta(days=2)
        self.task.save()
        self.assertEqual(self.task.due, self.timestamp + timedelta(days=2))
