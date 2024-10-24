from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Friendship
from user_data.models import UserProfile
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_friend(request, user_id):
    try:
        friend_user_profile = UserProfile.objects.get(user_id=user_id)  
        
        friendship, created = Friendship.objects.get_or_create(
            user=request.user.userprofile,
            friend=friend_user_profile
        )
        
        reciprocal_friendship, reciprocal_created = Friendship.objects.get_or_create(
            user=friend_user_profile,
            friend=request.user.userprofile
        )

        if created:
            return Response({'message': 'Friend added successfully!'}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'You are already friends with this user.'}, status=status.HTTP_400_BAD_REQUEST)
    
    except UserProfile.DoesNotExist:
        return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_friends(request):
    try:
        user_profile = request.user.userprofile 
        friends = Friendship.objects.filter(user=user_profile).select_related('friend')

        friend_data = [
            {
                'id': friend.friend.user.id, 
                'first_name': friend.friend.user.first_name,  
                'days_without_drinking': friend.friend.days_without_drinking,
                'picture': friend.friend.picture,
            }
            for friend in friends
        ]
        
        return Response(friend_data, status=status.HTTP_200_OK)
    
    except UserProfile.DoesNotExist:
        return Response({'message': 'UserProfile not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_friend(request, user_id):
    try:
        friend_user = UserProfile.objects.get(user_id=user_id)  
        
        friendship = Friendship.objects.get(user=request.user.userprofile, friend=friend_user)
        friendship.delete()
        return Response({'message': 'Friendship successfully removed!'}, status=status.HTTP_204_NO_CONTENT)
    except Friendship.DoesNotExist:
        return Response({'message': 'Friendship not found.'}, status=status.HTTP_404_NOT_FOUND)
    except UserProfile.DoesNotExist:
        return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
