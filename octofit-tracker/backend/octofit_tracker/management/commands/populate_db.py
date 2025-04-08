from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=1500),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=48),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=101),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=35),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=49),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team.objects.create(_id=ObjectId(), name='Blue Team')
        team2 = Team.objects.create(_id=ObjectId(), name='Gold Team')
        team1.members.set(users[:3])  # First three users in Blue Team
        team2.members.set(users[3:])  # Last two users in Gold Team

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, date=date(2025, 4, 1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, date=date(2025, 4, 2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90, date=date(2025, 4, 3)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30, date=date(2025, 4, 4)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, date=date(2025, 4, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team1, points=300),
            Leaderboard(_id=ObjectId(), team=team2, points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', description='High-intensity interval training', duration=120),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', description='Weightlifting and strength exercises', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))