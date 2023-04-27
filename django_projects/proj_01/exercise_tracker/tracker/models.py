from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    weight = models.PositiveIntegerField(default=0.0)
    weight_unit = models.ForeignKey(
        "Units",
        related_name="users_by_weight_unit",
        on_delete=models.SET_NULL,
        null=True,
    )

    height = models.PositiveIntegerField(default=0.0)
    height_unit = models.ForeignKey(
        "Units",
        related_name="users_by_height_unit",
        on_delete=models.SET_NULL,
        null=True,
    )


class Units(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=20)


class Exercise(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(default="")


class Set(models.Model):
    date_time = models.DateTimeField(null=True, auto_now_add=True)
    reps = models.PositiveIntegerField()
    # exercise =
    workout = models.ForeignKey("Workout", related_name="sets", on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=0)
    weight_units = models.ForeignKey(
        "Units",
        related_name="sets_by_weight_unit",
        on_delete=models.SET_NULL,
        null=True,
    )


class Workout(models.Model):
    user = models.ForeignKey(User, related_name="workouts", on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.id} : {self.name} : {self.reps}: {self.date_time}"
