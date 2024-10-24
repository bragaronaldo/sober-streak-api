from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    days_without_drinking = models.IntegerField(default=0)  
    last_increment_date = models.DateField(null=True, blank=True)
    picture = models.TextField(null=True, blank=True)

    def can_increment(self):
        if self.last_increment_date is None:
            return True
        return (timezone.now().date() - self.last_increment_date).days >= 1
