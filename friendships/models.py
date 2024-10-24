from django.db import models
from django.utils import timezone
from user_data.models import UserProfile

class Friendship(models.Model):
    user = models.ForeignKey(UserProfile, related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(UserProfile, related_name='friend_of', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')
