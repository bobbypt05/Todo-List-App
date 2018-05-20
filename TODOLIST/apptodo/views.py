from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

# Create your views here.
#read about decorators

from .forms import TodoForm
from .models import TodoModel

def HomeToDo(request):
	myTodoList = TodoModel.objects.order_by('id')
	form = TodoForm()
	#read about context
	context = {'myTodoList': myTodoList, 'form': form} 
	return render(request,'index.html',context)



@require_POST
def addNewTodo(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		my_new_todo = TodoModel(todotext=request.POST['text'])
		my_new_todo.save()

	return redirect('index')	


def complete_todo(request,todo_id):
	my_todo = TodoModel.objects.get(pk=todo_id)
	my_todo.complete = True
	my_todo.save()

	return redirect('index')

#filter in django

def delete_todo(request):
	TodoModel.objects.filter(complete__exact=True).delete()
	return redirect('index')	