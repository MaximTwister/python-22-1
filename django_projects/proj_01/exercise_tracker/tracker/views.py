from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse_lazy
from tracker.models import (
    Exercise,
    Set,
)
from django.views.generic import (
    ListView,
    FormView,
    DetailView,
)
from tracker.forms import ExerciseForm


# FBV
def exercise_list(request: HttpRequest):
    exercises = Exercise.objects.all()
    return render(
        request=request,
        template_name="tracker/exercise_list.html",
        context={"exercise_list": exercises},
    )


# CBV
class ExerciseListView(ListView):
    model = Exercise


class ExerciseFormView(FormView):
    form_class = ExerciseForm
    template_name = "tracker/exersice_form.html"
    success_url = reverse_lazy("list_all_exercises_cbv")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ExerciseDetailView(DetailView):
    # template name: `exercise_detail.html`
    # inside template context name: `exercise`
    model = Exercise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = self.get_object()
        context["sets"] = Set.objects.filter(exercise=exercise)
        return context
