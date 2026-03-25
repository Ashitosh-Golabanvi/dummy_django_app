import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

@method_decorator(csrf_exempt, name='dispatch')
class TodoCRUDView(View):

    # ✅ GET (All OR Single)
    def get(self, request, id=None):
        if id:
            try:
                todo = Todo.objects.get(id=id)
                data = {
                    "id": todo.id,
                    "title": todo.title,
                    "completed": todo.completed
                }
                return JsonResponse(data)
            except Todo.DoesNotExist:
                return JsonResponse({"error": "Not found"}, status=404)
        else:
            todos = list(Todo.objects.values())
            return JsonResponse(todos, safe=False)

    # ✅ CREATE
    def post(self, request):
        data = json.loads(request.body)
        todo = Todo.objects.create(
            title=data.get("title"),
            completed=data.get("completed", False)
        )
        return JsonResponse({"message": "created", "id": todo.id})

    # ✅ UPDATE
    def put(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        data = json.loads(request.body)

        todo.title = data.get("title", todo.title)
        todo.completed = data.get("completed", todo.completed)
        todo.save()

        return JsonResponse({"message": "updated"})

    # ✅ DELETE
    def delete(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        todo.delete()
        return JsonResponse({"message": "deleted"})