"""todoServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoApp.views import task_views
from todoApp.views.user_views import UserView
from todoApp.views.task_views import TaskView

task_view = TaskView.as_view()
user_view = UserView.as_view()

urlpatterns = [
    # path('admin/', admin.site.urls),
    # task paths
    path('tasks', task_view, name='post'),
    path('tasks/<int:userId>', task_view, name='get'),
    # user paths
    path('users', user_view, name='post'),
    path('users/<int:userId>', user_view, name='get'),
]
