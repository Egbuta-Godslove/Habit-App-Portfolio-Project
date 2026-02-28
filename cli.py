from habit import Habit
from repository import HabitRepository
from analytics import (
    calculate_streak,
    filter_by_periodicity,
    longest_streak_all_habits,
    habit_with_highest_streak
)


def run_cli():
    repo = HabitRepository()
    repo.insert_predefined_data()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Create habit")
        print("2. Complete habit")
        print("3. View all habits")
        print("4. View habits by periodicity")
        print("5. View longest streak for a habit")
        print("6. View all streaks")
        print("7. View habit with highest streak")
        print("8. Delete habit")
        print("9. Exit")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = input("Periodicity (daily/weekly): ")
            habit = Habit(name, periodicity)
            habit_id = repo.add_habit(habit)
            print(f"Habit created with ID {habit_id}")

        elif choice == "2":
            habit_id = int(input("Enter habit ID: "))
            repo.complete_habit(habit_id)
            print("Habit marked as completed.")

        elif choice == "3":
            habits = repo.get_habits()
            for h in habits:
                print(h)

        elif choice == "4":
            periodicity = input("Enter periodicity (daily/weekly): ")
            habits = repo.get_habits()
            filtered = filter_by_periodicity(habits, periodicity)
            for h in filtered:
                print(h)

        elif choice == "5":
            habit_id = int(input("Enter habit ID: "))
            habits = repo.get_habits()
            habit = next((h for h in habits if h[0] == habit_id), None)

            if habit:
                completions = repo.get_completions(habit_id)
                streak = calculate_streak(completions, habit[2])
                print(f"Longest streak: {streak}")
            else:
                print("Habit not found.")

        elif choice == "6":
            results = longest_streak_all_habits(repo)
            for name, streak in results.items():
                print(f"{name}: {streak}")

        elif choice == "7":
            result = habit_with_highest_streak(repo)
            if result:
                print(f"Top habit: {result[0]} with streak {result[1]}")
            else:
                print("No habits available.")

        elif choice == "8":
            habit_id = int(input("Enter habit ID to delete: "))
            repo.delete_habit(habit_id)
            print("Habit deleted.")

        elif choice == "9":
            repo.close()
            print("Goodbye!")
            break

        else:
            print("Invalid option.")