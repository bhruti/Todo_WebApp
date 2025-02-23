from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=1000)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.task