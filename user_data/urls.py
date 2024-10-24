from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.get_user_profile, name='profile'),
    path('update-profile', views.update_user_profile, name='update-profile'),
    path('ranking', views.increment_days_without_drinking, name='ranking'),
    path('search-user/<str:email>/', views.search_user_by_email, name='search_user_by_email'),
]
