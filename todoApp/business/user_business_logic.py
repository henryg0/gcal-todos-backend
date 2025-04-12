from django.forms.models import model_to_dict
from todoApp.models import User

class UserBusinessLogic:
    def __init__(self):
        pass

    def create_user(self, name, dob, email, password):
        user = User(name=name, dob=dob, email=email, password=password)
        user.save()
        return user

    def get_user_by_id(self, userId):
        user = User.objects.get(id=userId)
        return user
    
    def get_all_users(self):
        users = User.objects.all()

        return [model_to_dict(user) for user in users]