from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Khoj(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    input_value =  ArrayField(models.IntegerField(), default=list, blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.input_value)
