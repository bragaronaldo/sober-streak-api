from django.urls import path
from .views import add_friend, remove_friend, list_friends

urlpatterns = [
    path('add-friend/<int:user_id>', add_friend, name='add-friend'),
    path('remove-friend/<int:user_id>', remove_friend, name='remove-friend'),
    path('list-friends', list_friends, name='list-friends'),
]
