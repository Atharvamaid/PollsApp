from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Poll(models.Model):
    poll = models.TextField(max_length=200)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op1_cnt = models.IntegerField(default=0)
    op2_cnt = models.IntegerField(default=0)
    op3_cnt = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.poll} by {self.user}'
