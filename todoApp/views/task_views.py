from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from todoApp.business.task_business_logic import TaskBusinessLogic

import json

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    def __init__(self):
        super().__init__()
        self.taskBusinessLogic = TaskBusinessLogic()

    def get(self, request, userId):
        return self._get_tasks_by_user_id(request, userId)

    def post(self, request):
        try:
            if request.method == 'POST' and request.META.get('HTTP_X_HTTP_METHOD_OVERRIDE') == 'DELETE':
                return self.delete(request)
            else:
                return self.create(request)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def delete(self, request):
        try:
            self._delete_task_by_id(request)
            return JsonResponse({"message": "Task deleted successfully" + str(request.POST['id'])}, status=200)
        except Exception as e:
            return JsonResponse({"error": "Error when deleting task: " + str(e)}, status=500)

    def create(self, request):
        try:
            task = self._create_task(request)
            return JsonResponse({"message": "Task created successfully with taskId: " + str(task.id)}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": "Error when creating task: " + str(e)}, status=500)

    def _get_tasks_by_user_id(self, request, userId):
        try:
            tasks = self.taskBusinessLogic.get_all_tasks(userId).values()
            return JsonResponse(list(tasks), safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    def _delete_task_by_id(self, request):
        try:
            data = json.loads(request.body)
            self.taskBusinessLogic.delete_task(data['id'])
            return JsonResponse({"message": "Task deleted successfully with taskId: " + str(data['id'])})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    def _create_task(self, request):
        data = json.loads(request.body)
        description = data.get('description')
        return self.taskBusinessLogic.create_task(data['userId'], data['title'], description)
