from todoApp.models import Task, User

"""
Handles CRUD operations on tasks
""" 
class TaskBusinessLogic:
    def __init__(self):
        pass

    def create_task(self, userId, title, description):
        user = User.objects.get(id=userId)
        task = Task(user=user, title=title, description=description)
        task.save()
        return task

    def get_all_tasks(self, userId):
        user = User.objects.get(id=userId)    
        return Task.objects.filter(user=user)

    def get_task_by_id(self, id):
        return Task.objects.get(id=id)

    def update_task_status(self, status):
        task = Task.objects.get(id=id)
        task.status = status
        task.save()
        return task

    def delete_task(self, id):
        task = Task.objects.get(id=id)
        task.delete()