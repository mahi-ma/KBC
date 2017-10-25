from django.db import models


class Question(models.Model):
    ques = models.CharField(max_length=500)
    opA = models.CharField(max_length=200)
    opB = models.CharField(max_length=200)
    opC = models.CharField(max_length=200)
    opD = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    isUsed = models.BooleanField(default=False)


