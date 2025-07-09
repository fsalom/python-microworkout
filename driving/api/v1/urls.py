from django.urls import include, path
from . import workouts

urlpatterns = [
    # path('users/', include('driving.api.v1.users.urls')),
    path('workouts/',        workouts.workout_list_create, name='workout-list-create'),
    path('workouts/<uuid:id>/', workouts.workout_retrieve,    name='workout-detail'),
]
