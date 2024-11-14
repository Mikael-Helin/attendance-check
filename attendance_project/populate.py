# This script populates the database with fake users

import os
import shutil
import random
from datetime import datetime, timedelta
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_project.settings')
django.setup()

from attendance.models import User, Attendance

# Fake data
first_names = ["Some", "Another", "One", "Two", "Three", "Student", "Teacher", "No"]
last_names = ["People", "Lexicon", "Reply"]

people = {}
for first_name in first_names:
    for last_name in last_names:
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        people[first_name + " " + last_name] = email

# Reset the database
if os.path.isfile("db.sqlite3"):
    os.remove("db.sqlite3")

if os.path.isdir("attendance/migrations"):
    shutil.rmtree("attendance/migrations")

# Run migrations
os.system("python manage.py makemigrations attendance")
os.system("python manage.py migrate")

# Insert fake users and attendance records
for name, email in people.items():
    first_name, last_name = name.split()
    user = User.objects.create(firstname=first_name, lastname=last_name, email=email)

    # Generate and add fake attendance records
    for i in range(5):
        # Create a random datetime within the past year
        random_days = random.randint(0, 365)
        random_seconds = random.randint(0, 86400)  # seconds in a day
        fake_timestamp = datetime.now() - timedelta(days=random_days, seconds=random_seconds)
        
        Attendance.objects.create(user=user, timestamp=fake_timestamp)

print("Database populated with fake users and attendance records.")
print("Type 'python manage.py runserver' to start the server.")
print("And navigate to http://localhost:8000/")
