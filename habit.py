from datetime import datetime


class Habit:
    """
    Represents a habit with a name and periodicity.
    Periodicity can be 'daily' or 'weekly'.
    """

    def __init__(self, name: str, periodicity: str, created_at=None, habit_id=None):
        self.habit_id = habit_id
        self.name = name
        self.periodicity = periodicity.lower()
        self.created_at = created_at or datetime.now()

        if self.periodicity not in ["daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")

    def __repr__(self):
        return f"Habit(name='{self.name}', periodicity='{self.periodicity}')"