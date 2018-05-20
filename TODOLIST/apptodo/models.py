from django.db import models

# Create your models here.

class TodoModel(models.Model):
	complete = models.BooleanField(default=False)

	todotext = models.CharField(max_length=50)

	def __str__(self):
		return self.todotext