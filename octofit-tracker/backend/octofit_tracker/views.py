from rest_framework import viewsets
from django.http import JsonResponse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

def api_root(request):
    return JsonResponse({
        "users": "https://humble-happiness-4qjr7vw796729w9-8000.app.github.dev/api/users/",
        "teams": "https://humble-happiness-4qjr7vw796729w9-8000.app.github.dev/api/teams/",
        "activities": "https://humble-happiness-4qjr7vw796729w9-8000.app.github.dev/api/activities/",
        "leaderboard": "https://humble-happiness-4qjr7vw796729w9-8000.app.github.dev/api/leaderboard/",
        "workouts": "https://humble-happiness-4qjr7vw796729w9-8000.app.github.dev/api/workouts/",
        "localhost_users": "http://localhost:8000/api/users/",
        "localhost_teams": "http://localhost:8000/api/teams/",
        "localhost_activities": "http://localhost:8000/api/activities/",
        "localhost_leaderboard": "http://localhost:8000/api/leaderboard/",
        "localhost_workouts": "http://localhost:8000/api/workouts/"
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
