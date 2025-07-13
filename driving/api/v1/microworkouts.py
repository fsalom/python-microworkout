from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from application.services.microworkouts import MicroWorkoutService
from application.ports.microworkouts import MicroWorkoutRepository
from driven.db.microworkouts.repository import DjangoORMMicroWorkoutRepository
from .schemas import (
    MicroWorkoutIn,
    MicroWorkoutOut,
    MicroRoundOut,
)

_service = MicroWorkoutService(repo=DjangoORMMicroWorkoutRepository())


@require_http_methods(['GET', 'POST'])
@login_required
def microworkout_list_create(request):
    if request.method == 'GET':
        data = _service.list_for_user(str(request.user.id))
        return JsonResponse(data, safe=False)

    import json
    body = json.loads(request.body)
    mw = _service.create(
        str(request.user.id),
        body.get('exercise_id', ''),
        body.get('interval_minutes', 0),
        body.get('rounds', 0),
    )
    return JsonResponse(MicroWorkoutOut(**mw).dict(), status=201)


@require_http_methods(['GET'])
@login_required
def microworkout_retrieve(request, id):
    mw = _service.get_by_id(str(request.user.id), str(id))
    if not mw:
        return JsonResponse({'detail': 'Not found'}, status=404)
    return JsonResponse(MicroWorkoutOut(**mw).dict(), status=200)


@require_http_methods(['POST'])
@login_required
def microworkout_complete_round(request, id, round_id):
    updated = _service.complete_round(
        str(request.user.id), str(id), str(round_id)
    )
    if not updated:
        return JsonResponse({'detail': 'Not found'}, status=404)
    return JsonResponse(MicroWorkoutOut(**updated).dict(), status=200)