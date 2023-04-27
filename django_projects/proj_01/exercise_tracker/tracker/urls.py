from django.urls import path
from tracker.views import (
    exercise_list,
    ExerciseListView,
    ExerciseFormView,
)


"http://127.0.0.1:8000/tracker/exercises-fbv/"
"http://127.0.0.1:8000/tracker/exercises-cbv/"
"http://127.0.0.1:8000/tracker/add-exercise/"
urlpatterns = [
    path("exercises-fbv/", exercise_list, name="list_all_exercises_fbv"),
    path("add-exercise/", ExerciseFormView.as_view(), name="exercise_form"),
    path("exercises-cbv/", ExerciseListView.as_view(), name="list_all_exercises_cbv"),
]
