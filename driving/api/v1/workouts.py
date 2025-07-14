from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from pydantic import ValidationError

from application.services.workouts import WorkoutService
from application.ports.workouts import WorkoutRepository
from driven.db.workouts.repository import DjangoORMWorkoutRepository
from .schemas import WorkoutIn, WorkoutOut

_service = WorkoutService(repo=DjangoORMWorkoutRepository())


@require_http_methods(["GET", "POST"])
@login_required
def workout_list_create(request):
    if request.method == "GET":
        data = _service.list_for_user(str(request.user.id))
        return JsonResponse(data, safe=False, status=200)

    try:
        payload = WorkoutIn.parse_raw(request.body)
    except ValidationError as e:
        return JsonResponse({"errors": e.errors()}, status=400)

    created = _service.create(str(request.user.id), payload)
    return JsonResponse(WorkoutOut(**created).dict(), status=201)


@require_http_methods(["GET"])
@login_required
def workout_retrieve(request, id):
    found = _service.get_by_id(str(request.user.id), str(id))
    if not found:
        return JsonResponse({"detail": "Not found"}, status=404)
    return JsonResponse(WorkoutOut(**found).dict(), status=200)


@require_http_methods(["GET"])
@login_required
def workout_history(request, exercise_id):
    data = _service.list_exercise_history(str(request.user.id), exercise_id)
    return JsonResponse(data, safe=False, status=200)