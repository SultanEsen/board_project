# from django.db import models
# from django.contrib.auth.models import User
#
#
# class AdvUser(models.Model):
#     is_activated = models.BooleanField(default=True)
#     users = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
# class Spare(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class Machine(models.Model):
#     name = models.CharField(max_length=30)
#     spares = models.ManyToManyField(Spare)
