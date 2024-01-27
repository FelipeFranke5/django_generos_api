import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.utils import IntegrityError
from .models import Genre


@csrf_exempt
@require_http_methods(["GET", "POST"])
def genre_view(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = [
            {"id": genre.id, "name": genre.name, "date_created": genre.date_created}
            for genre in genres
        ]
        return JsonResponse(data, safe=False)
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse(
                data={
                    "code": 0,
                    "return_code": 0,
                    "message": "Request body is required",
                    "exception": "JSONDecodeError",
                },
                status=400,
            )
        name = data.get("name")

        if not name:
            return JsonResponse(
                data={
                    "code": 0,
                    "return_code": 1,
                    "message": "Name is required",
                    "exception": "None",
                },
                status=400,
            )

        try:
            new_genre = Genre.objects.create(name=name)
        except IntegrityError:
            return JsonResponse(
                data={
                    "code": 0,
                    "return_code": 2,
                    "message": "A genre with this name already exists",
                    "exception": "IntegrityError",
                },
                status=400,
            )

        return JsonResponse(
            data={
                "code": 1,
                "return_code": 0,
                "message": "Created new genre",
                "data": {
                    "id": new_genre.id,
                    "name": new_genre.name,
                    "date_created": new_genre.date_created,
                },
            },
            status=201,
        )


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return JsonResponse(
            data={
                "code": 0,
                "return_code": 3,
                "message": "Genre not found",
                "exception": "DoesNotExist",
            },
            status=404,
        )

    if request.method == "GET":
        data = {"id": genre.pk, "name": genre.name, "date_created": genre.date_created}
        return JsonResponse(data=data)
    if request.method == "PUT":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse(
                data={
                    "code": 0,
                    "return_code": 0,
                    "message": "Request body is required",
                    "exception": "JSONDecodeError",
                },
                status=400,
            )
        name = data.get("name")

        if not name:
            return JsonResponse(
                data={
                    "code": 0,
                    "return_code": 1,
                    "message": "Name is required",
                    "exception": "None",
                },
                status=400,
            )

        if genre.name.lower().strip() == name.lower().strip():
            return JsonResponse(
                data={
                    "code": 0,
                    "return_code": 4,
                    "message": "The name should be different for a PUT request",
                    "current_name": genre.name,
                    "exception": "None",
                },
                status=400,
            )

        genre_old_name = genre.name
        genre.name = name
        genre.save()
        return JsonResponse(
            data={
                "code": 1,
                "return_code": 1,
                "message": "Changed genre's name",
                "data": {
                    "id": genre.id,
                    "old_name": genre_old_name,
                    "new_name": genre.name,
                    "date_created": genre.date_created,
                },
            },
            status=200,
        )
    if request.method == "DELETE":
        genre.delete()
        return JsonResponse(
            data={
                "code": 1,
                "return_code": 2,
                "message": "Deleted genre",
            },
            status=204,
        )
