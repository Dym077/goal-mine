from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import GoalForm
from .models import Goal

class TestGoalViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.goal = Goal(title="Goal title", author=self.user,
                         excerpt="Goal excerpt",
                         body="Goal body", status=1)
        self.goal.save()

    def test_render_goal_detail_page_with_goal_form(self):
        response = self.client.get(reverse(
            'goal_detail', args=['goal-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Goal title", response.body)
        self.assertIn(b"Goal body", response.body)
        self.assertIsInstance(
            response.body['goal_form'], GoalForm)
        print(response.context)