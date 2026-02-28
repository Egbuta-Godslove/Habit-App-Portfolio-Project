import sqlite3
from datetime import datetime
from habit import Habit


class HabitRepository:
    def __init__(self, db_name="habits.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            periodicity TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            completed_at TEXT NOT NULL,
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
        """)

        self.conn.commit()

    def add_habit(self, habit):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO habits (name, periodicity, created_at) VALUES (?, ?, ?)",
            (habit.name, habit.periodicity, habit.created_at.isoformat())
        )
        self.conn.commit()
        return cursor.lastrowid

    def complete_habit(self, habit_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
            (habit_id, datetime.now().isoformat())
        )
        self.conn.commit()

    def get_habits(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM habits")
        return cursor.fetchall()

    def get_completions(self, habit_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT completed_at FROM completions WHERE habit_id = ?",
            (habit_id,)
        )
        return cursor.fetchall()

    def delete_habit(self, habit_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM completions WHERE habit_id = ?", (habit_id,))
        cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        self.conn.commit()

    def update_habit(self, habit_id, new_name, new_periodicity):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE habits SET name = ?, periodicity = ? WHERE id = ?",
            (new_name, new_periodicity, habit_id)
        )
        self.conn.commit()

    def insert_predefined_data(self):
        from datetime import timedelta

        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM habits")
        count = cursor.fetchone()[0]

        # Prevent duplicate insertion
        if count > 0:
            return

        # Create habits
        daily_id = self.add_habit(Habit("Drink Water", "daily"))
        weekly_id = self.add_habit(Habit("Exercise", "weekly"))

        # Insert 4 weeks of daily completions
        for i in range(28):
            date = datetime.now() - timedelta(days=i)
            self.conn.execute(
                "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
                (daily_id, date.isoformat())
            )

        # Insert 4 weekly completions
        for i in range(4):
            date = datetime.now() - timedelta(weeks=i)
            self.conn.execute(
                "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
                (weekly_id, date.isoformat())
            )

        self.conn.commit()

    def close(self):
        self.conn.close()