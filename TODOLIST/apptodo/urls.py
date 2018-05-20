from django.urls import path

from . import views

urlpatterns = [

    path('',views.HomeToDo,name="index"),
    path('add/',views.addNewTodo,name="addtodo"),
    path('complete/<todo_id>',views.complete_todo,name="complete"),
    path('delete/',views.delete_todo,name="delete")
]