# Create your views here.
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from todoApp.business.user_business_logic import UserBusinessLogic

import json

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def __init__(self):
        super().__init__()        
        self.userBusinessLogic = UserBusinessLogic()

    def get(self, request, userId=None):
        try:
            if not userId:
                return JsonResponse(self.userBusinessLogic.get_all_users(), safe=False, status=200)
            return self.__get_user_by_id(userId)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def post(self, request):
        return self.__create_user(request)

    def _create_user(self, request):
        try:
            data = json.loads(request.body)
            user = self.userBusinessLogic.create_user(data['name'], data['dob'], data['email'], data['password'])
            return JsonResponse({"message": "User created successfully with userId: " + str(user.id)}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def _get_user_by_id(self, userId):
        user = self.userBusinessLogic.get_user_by_id(userId)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        return JsonResponse(model_to_dict(user))
