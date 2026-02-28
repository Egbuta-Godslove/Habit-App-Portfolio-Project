import unittest
from analytics import calculate_streak
from habit import Habit
from datetime import datetime, timedelta


class TestHabit(unittest.TestCase):

    def test_create_habit(self):
        habit = Habit("Read", "daily")
        self.assertEqual(habit.name, "Read")
        self.assertEqual(habit.periodicity, "daily")


class TestAnalytics(unittest.TestCase):

    def test_daily_streak(self):
        dates = [
            (datetime.now().isoformat(),),
            ((datetime.now() - timedelta(days=1)).isoformat(),),
            ((datetime.now() - timedelta(days=2)).isoformat(),)
        ]
        streak = calculate_streak(dates, "daily")
        self.assertEqual(streak, 3)

    def test_weekly_streak(self):
        dates = [
            (datetime.now().isoformat(),),
            ((datetime.now() - timedelta(weeks=1)).isoformat(),),
            ((datetime.now() - timedelta(weeks=2)).isoformat(),)
        ]
        streak = calculate_streak(dates, "weekly")
        self.assertEqual(streak, 3)


if __name__ == "__main__":
    unittest.main()