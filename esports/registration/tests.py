
from django.test import TestCase
from .models import Registrant, Team

class RegistrantModelTest(TestCase):
    def test_create_registrant(self):
        registrant = Registrant.objects.create(
            first_name='Jane',
            last_name='Doe',
            student_email='jane@example.com',
            password='password123',
            student_id='12345',
            twitch='janedoe'
        )
        self.assertEqual(str(registrant), 'Jane Doe')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(
            name='Team A',
            captain='Alice'
        )
        self.assertEqual(team.name, 'Team A')
