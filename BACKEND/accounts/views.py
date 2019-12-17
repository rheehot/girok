from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer, UserDetailSerializer
from logs.serializers import LogSerializer, TodoListSerializer, TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


# Create your views here.
@api_view(['GET'])
def users(request):
    User = get_user_model()
    users_all = User.objects.all()
    serializer = UserSerializer(users_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def user_followers(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    followers = user.followers.all()
    serializer = UserSerializer(followers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_followings(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    followings = user.followings.all()
    serializer = UserSerializer(followings, many=True)
    return Response(serializer.data)

