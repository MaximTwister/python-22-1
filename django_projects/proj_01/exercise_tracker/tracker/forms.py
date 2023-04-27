from django import forms
from tracker.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "description"]
