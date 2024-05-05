from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from .forms import GoalForm


class TestGoalForm(TestCase):

    def test_form_is_valid(self):
        goal_form = GoalForm({'body': 'This should not be read by any other than the superuser'})
        self.assertTrue(goal_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        goal_form = GoalForm({'body': ''})
        self.assertFalse(goal_form.is_valid(), msg="Form is valid")    