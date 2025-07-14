from django.urls import include, path
from . import workouts, microworkouts

urlpatterns = [
    # path('users/', include('driving.api.v1.users.urls')),
    path('workouts/',        workouts.workout_list_create, name='workout-list-create'),
    path('workouts/<uuid:id>/', workouts.workout_retrieve,    name='workout-detail'),
    path('workouts/history/<str:exercise_id>/', workouts.workout_history, name='workout-history'),
    path('microworkouts/', microworkouts.microworkout_list_create, name='microworkout-list-create'),
    path('microworkouts/<uuid:id>/', microworkouts.microworkout_retrieve, name='microworkout-detail'),
    path('microworkouts/<uuid:id>/rounds/<uuid:round_id>/complete/', microworkouts.microworkout_complete_round, name='microworkout-complete-round'),
]
