"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tasks_index_view, name = 'index'),
    path('article/<int:pk>', views.tasks_find_view, name = 'task_view'),
    path('article/add/', views.tasks_add_view, name = 'task_add'),
    path('article/delete/<int:pk>', views.tasks_delete_view, name = 'task_delete'),
    path('article/update/<int:pk>', views.tasks_update_view, name = 'task_update')
]
