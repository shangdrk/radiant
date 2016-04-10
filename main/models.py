from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Connection(models.Model):
    user_one = models.ForeignKey(User, related_name='initiator', on_delete=models.CASCADE)
    user_two = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    one_to_two = models.TextField()
    two_to_one = models.TextField()

    def __str__(self):
        if self.is_valid:
            name_one = self.user_one.username
            name_two = self.user_two.username
            return "Connection between " + str(name_one) + " and " + str(name_two)
        else:
            return "The connection is no longer valid"

    def is_valid(self):
        return self.user_one.is_active and self.user_two.is_active


class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_value = models.IntegerField()
    friends = models.ManyToManyField(User, related_name='friend')

    def add_friend(self, friend):
        self.friends.add(friend)