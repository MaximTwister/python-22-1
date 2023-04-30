from random import randint

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tracker.models import (
    UserProfile,
    Set,
    Workout,
    Exercise,
    Unit,
)


class Command(BaseCommand):
    help = "Description for my Test Command"

    def add_arguments(self, parser):
        parser.add_argument(
            "sets",
            type=int,
            help="Number of sets for each exercise in the workout."
        )

    def handle(self, *args, **options):
        sets = options.get("sets")

        # Handle User
        # user = User.objects.first()
        user = User.objects.create(
            username="Maksym",
            password="12345",
        )

        # Handle UserProfile
        user_profile = UserProfile.objects.create(user=user)

        # Handle Workout
        workout = Workout.objects.create(user_profile=user_profile)

        # Handle Unit
        unit = Unit.objects.create(
            short_name="kg",
            name="kilogram",
        )

        # Handle Exercises
        ex_1 = Exercise.objects.create(
            name="Exercise Four",
            description="Exercise Four is hard",
        )
        ex_2 = Exercise.objects.create(
            name="Exercise Five",
            description="Exercise Five is easy one",
        )
        ex_3 = Exercise.objects.create(
            name="Exercise Six",
            description="Exercise Six is for advanced guys.",
        )

        # Handle Sets
        sets = [
            Set(reps=randint(10, 55), exercise=ex, workout=workout, weight=10.0, weight_unit=unit)
            for ex in [ex_1, ex_2, ex_3]
            for _ in range(sets)
        ]

        Set.objects.bulk_create(sets)

        self.stdout.write(self.style.SUCCESS("Workout was successfully created"))
