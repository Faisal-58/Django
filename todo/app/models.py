from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
