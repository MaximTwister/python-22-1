from django.urls import path
from tracker.views import (
    exercise_list,
    ExerciseListView,
    ExerciseFormView,
    ExerciseDetailView,
)


"http://127.0.0.1:8000/tracker/exercises-fbv/"
"http://127.0.0.1:8000/tracker/exercises-cbv/"
"http://127.0.0.1:8000/tracker/add-exercise/"
"http://127.0.0.1:8000/tracker/exercise/3/"
urlpatterns = [
    path("exercises-fbv/", exercise_list, name="list_all_exercises_fbv"),
    path("add-exercise/", ExerciseFormView.as_view(), name="exercise_form"),
    path("exercises/", ExerciseListView.as_view(), name="exercises_list"),
    path("exercise/<int:pk>/", ExerciseDetailView.as_view(), name="exercise_detail")
]

# Generic detail view ExerciseDetailView must be called with either
# an object pk==id or a slug in the URLconf.
