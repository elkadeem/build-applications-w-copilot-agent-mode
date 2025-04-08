from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return ObjectId(value)

class User(models.Model):
    _id = ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Team(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    date = models.DateField()

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes
