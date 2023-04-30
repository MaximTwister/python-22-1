from collections import defaultdict

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    weight = models.PositiveIntegerField(default=0.0)
    weight_unit = models.ForeignKey(
        "Unit",
        related_name="users_by_weight_unit",
        on_delete=models.SET_NULL,
        null=True,
    )

    height = models.PositiveIntegerField(default=0.0)
    height_unit = models.ForeignKey(
        "Unit",
        related_name="users_by_height_unit",
        on_delete=models.SET_NULL,
        null=True,
    )


class Unit(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=20)


class Exercise(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(default="")


class Set(models.Model):
    date_time = models.DateTimeField(null=True, auto_now_add=True)
    reps = models.PositiveIntegerField()
    exercise = models.ForeignKey("Exercise", related_name="sets", on_delete=models.CASCADE)
    workout = models.ForeignKey("Workout", related_name="sets", on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=0)
    weight_unit = models.ForeignKey(
        "Unit",
        related_name="sets_by_weight_unit",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.reps} reps of {self.exercise.name} at {self.weight}{self.weight_units.short_name}"

    class Meta:
        ordering = ['date_time']


class Workout(models.Model):
    user_profile = models.ForeignKey("UserProfile", related_name="workouts", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(default="", blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s workout on {self.date}"

    def get_exercises_with_sets(self):
        # {"ExerciseName01": [12, 23, 10], "ExerciseName02": [22, 44, 19], ...}
        exercises_with_sets = defaultdict(list)

        # `select_related` solves `N+1 Query Problem`
        sets = self.sets.select_related("exercise", "weight_unit").all()

        for set_instance in sets:
            exercises_with_sets[set_instance.exercise].append(set_instance)

        return exercises_with_sets
