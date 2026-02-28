from datetime import datetime, timedelta


def calculate_streak(completion_dates, periodicity):
    if not completion_dates:
        return 0

    dates = sorted([datetime.fromisoformat(d[0]) for d in completion_dates])

    streak = 1
    max_streak = 1

    for i in range(1, len(dates)):
        diff = dates[i] - dates[i - 1]

        if periodicity == "daily" and diff <= timedelta(days=1):
            streak += 1
        elif periodicity == "weekly" and diff <= timedelta(days=7):
            streak += 1
        else:
            streak = 1

        max_streak = max(max_streak, streak)

    return max_streak


def filter_by_periodicity(habits, periodicity):
    return list(filter(lambda h: h[2] == periodicity, habits))


def longest_streak_all_habits(repo):
    habits = repo.get_habits()
    results = {}

    for habit in habits:
        habit_id = habit[0]
        name = habit[1]
        periodicity = habit[2]

        completions = repo.get_completions(habit_id)
        streak = calculate_streak(completions, periodicity)

        results[name] = streak

    return results


def habit_with_highest_streak(repo):
    all_streaks = longest_streak_all_habits(repo)

    if not all_streaks:
        return None

    return max(all_streaks.items(), key=lambda x: x[1])