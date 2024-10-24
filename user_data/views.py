# views.py do app de autenticação
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from user_data.models import UserProfile
from user_data.serializers import UserProfileSerializer 
from django.utils import timezone
from django.contrib.auth.models import User 

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_user_profile(request):
    user = request.user 
    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        return Response({'error': 'User profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

    profile_serializer = UserProfileSerializer(user_profile) 
    return Response(profile_serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

    first_name = request.data.get('first_name')
    if first_name is not None:
        user.first_name = first_name
        user.save()

    picture = request.data.get('picture')
    if picture is not None:
        user_profile.picture = picture
        user_profile.save()

    profile_serializer = UserProfileSerializer(user_profile)
    return Response(profile_serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def increment_days_without_drinking(request):
    user = request.user 
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

    drank = request.data.get('drank', None)

    if drank is None:
        return Response({'error': "The 'drank' parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

    if not isinstance(drank, bool):
        return Response({'error': "The 'drank' parameter must be a boolean (true/false)."}, status=status.HTTP_400_BAD_REQUEST)

    if drank:
        user_profile.days_without_drinking = 0
        user_profile.last_increment_date = timezone.now().date()  
    else:
        # if not user_profile.can_increment():
        #     return Response({'error': 'You can only increment once per day.'}, status=status.HTTP_403_FORBIDDEN)

        user_profile.days_without_drinking += 1  
        user_profile.last_increment_date = timezone.now().date()  

    user_profile.save()

    return Response({'days_without_drinking': user_profile.days_without_drinking}, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_user_by_email(request, email):
    try:
        user = User.objects.get(email=email)
        user_profile = UserProfile.objects.get(user=user)

        response_data = {
            'id': user.id,
            'first_name': user.first_name,
            'days_without_drinking': user_profile.days_without_drinking,
            'picture': user_profile.picture,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User profile does not exist'}, status=status.HTTP_404_NOT_FOUND)
