from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from datetime import date, timedelta
import json


from .scoring import calculate_scores


class ScoringTests(TestCase):
    def test_urgency_calculation(self):
        """Task with closer deadline must have higher urgency"""
        today = date.today()

        tasks = [
            {
                "task_id": "t1",
                "title": "Urgent Task",
                "due_date": today + timedelta(days=1),
                "estimated_hours": 3,
                "importance": 8,
                "dependencies": []
            },
            {
                "task_id": "t2",
                "title": "Less Urgent Task",
                "due_date": today + timedelta(days=20),
                "estimated_hours": 3,
                "importance": 8,
                "dependencies": []
            }
        ]

        weights = {"w_u": 0.4, "w_i": 0.3, "w_e": 0.2, "w_d": 0.1}
        result = calculate_scores(tasks, weights)

        self.assertGreater(result[0]["urgency"], result[1]["urgency"])


    def test_effort_calculation(self):
        """Low effort task must have higher effort score"""
        today = date.today()

        tasks = [
            {
                "task_id": "t1",
                "title": "Quick Task",
                "due_date": today,
                "estimated_hours": 2,
                "importance": 5,
                "dependencies": []
            },
            {
                "task_id": "t2",
                "title": "Big Task",
                "due_date": today,
                "estimated_hours": 8,
                "importance": 5,
                "dependencies": []
            }
        ]

        weights = {"w_u": 0.4, "w_i": 0.3, "w_e": 0.2, "w_d": 0.1}
        result = calculate_scores(tasks, weights)

        self.assertGreater(result[0]["effort"], result[1]["effort"])


    def test_score_sorting(self):
        """Higher score task must be first after sorting"""
        today = date.today()

        tasks = [
            {
                "task_id": "t1",
                "title": "High Importance",
                "due_date": today,
                "estimated_hours": 3,
                "importance": 9,
                "dependencies": []
            },
            {
                "task_id": "t2",
                "title": "Low Importance",
                "due_date": today,
                "estimated_hours": 3,
                "importance": 2,
                "dependencies": []
            }
        ]

        weights = {"w_u": 0.4, "w_i": 0.3, "w_e": 0.2, "w_d": 0.1}
        result = calculate_scores(tasks, weights)

        self.assertGreater(result[0]["score"], result[1]["score"])


class APITests(TestCase):

    def setUp(self):
        today = date.today()
        self.sample_tasks = [
            {
                "task_id": "t1",
                "title": "Fix bug",
                "due_date": str(today + timedelta(days=1)),
                "estimated_hours": 2,
                "importance": 8,
                "dependencies": []
            },
            {
                "task_id": "t2",
                "title": "Write docs",
                "due_date": str(today + timedelta(days=5)),
                "estimated_hours": 4,
                "importance": 5,
                "dependencies": ["t1"]
            }
        ]


    def test_analyze_api(self):
        """Analyze API must return a list with score"""
        response = self.client.post(
            "/api/tasks/analyze/?strategy=smart",
            data=json.dumps(self.sample_tasks),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertIn("score", data[0])


    def test_suggest_api(self):
        """Suggest API must return tasks with reason"""
        response = self.client.post(
            "/api/tasks/suggest/?strategy=smart",
            data=json.dumps(self.sample_tasks),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertIn("reason", data[0])
