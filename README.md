# Habit Tracking Application Portfolio Project

## GitHub Repository

https://github.com/Egbuta-Godslove/Habit-App-Portfolio-Project

---

# Overview

The Habit Tracking Application is a Python-based software project designed to help users build and maintain positive habits. The application allows users to create habits, record habit completions, and analyse their progress over time.

The system was developed using a modular software architecture. Each part of the application has a specific responsibility such as habit creation, database storage, analytics, and user interaction through a command-line interface (CLI).

This project demonstrates important software development concepts including modular programming, database management, functional programming, and automated testing.

---

# Project Objectives

The main objectives of this project are:

* Allow users to create and manage habits
* Record habit completion events
* Track habit streaks and progress
* Store habit data in a reliable database
* Implement unit tests to verify system functionality

---

# Key Features

### Habit Management

Users can:

* Create habits
* Edit habits
* Delete habits
* View all habits
* Mark habits as completed

### Analytics

The analytics module allows users to:

* Calculate current streaks
* Calculate longest streaks
* Filter habits by periodicity
* Analyse habit completion patterns

The streak calculation respects the habit's periodicity (daily or weekly).

---

# Technologies Used

This project was developed using the following technologies:

* Python 3
* SQLite Database
* Command Line Interface (CLI)
* Python unittest framework
* Git & GitHub for version control

---

# Project Architecture

The application follows a modular structure to improve readability and maintainability.

Habit-App-Portfolio-Project/
│
├── main.py
├── cli.py
├── habit.py
├── repository.py
├── analytics.py
│
├── data/
│   └── habits.db
│
├── tests/
│   └── test_habits.py
│
├── screenshots/
│   ├── create_habit.png
│   ├── complete_habit.png
│   ├── analytics_results.png
│   └── unit_tests.png
│
├── .gitignore
└── README.md

Each module performs a specific role:

* **habit.py** – defines the Habit class
* **repository.py** – manages database operations
* **analytics.py** – performs habit analysis and streak calculations
* **cli.py** – handles command-line user interaction
* **main.py** – program entry point

---

# Database Design

The application uses SQLite to store habit data.

## Habits Table

| Field       | Description         |
| ----------- | ------------------- |
| id          | Unique habit ID     |
| name        | Habit name          |
| periodicity | Daily or Weekly     |
| created_at  | Habit creation time |

## Completions Table

| Field        | Description          |
| ------------ | -------------------- |
| id           | Completion event ID  |
| habit_id     | Associated habit     |
| completed_at | Completion timestamp |

This database structure allows the system to track habit completion history.

---

# Predefined Test Data

To test the system, predefined habits with **four weeks of completion data** were added.

This time-series data is used to verify that streak calculations and analytics functions work correctly.

---

# Running the Application

Follow these steps to run the program.

### 1 Clone the repository

git clone https://github.com/Egbuta-Godslove/Habit-App-Portfolio-Project.git

### 2 Navigate to the project directory

cd Habit-App-Portfolio-Project

### 3 Run the application

python main.py

---

# Running Unit Tests

Unit tests are implemented using Python's **unittest** framework.

Run the tests using:

python -m unittest discover tests

The unit tests verify:

* Habit creation
* Habit editing
* Habit deletion
* Habit completion tracking
* Analytics functionality
* Streak calculations

---

# Screenshots

Screenshots demonstrating the application functionality are included in the **screenshots folder**.

These include:

* Habit creation
* Habit completion
* Analytics results
* Unit test results

---

# Future Improvements

Possible improvements for the application include:

* Graphical User Interface (GUI)
* Web-based version of the application
* Data visualisation charts
* Mobile application support
* Cloud database integration

---

# Learning Outcomes

Through this project the following skills were developed:

* Python programming
* Software architecture design
* Database integration
* Functional programming
* Unit testing
* Software documentation
* Version control using Git and GitHub

---

# Author

Godslove Egbuta
Cybersecurity & Software Development Student
