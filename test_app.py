
import unittest
import app

class TestAssignmentTracker(unittest.TestCase):

    def setUp(self):
        app.assignments.clear()

    def test_add_assignment(self):
        app.add_assignment("Adaptive Software Engineering", "30-11-2026")
        self.assertEqual(len(app.assignments), 1)

    def test_mark_completed(self):
        app.add_assignment("Adaptive Software Engineering", "30-11-2026")
        app.mark_completed(0)
        self.assertEqual(app.assignments[0]["status"], "Completed")

    def test_invalid_assignment(self):
        result = app.mark_completed(5)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
