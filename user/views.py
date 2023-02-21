from django.shortcuts import render

from django.db.migrations import serializer
from django.contrib.auth import login, authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from user.serializers import UserSerializer


class UserView(APIView):  # CBV 방식
    permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    # TODO: 회원 조회
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    # TODO: 회원 가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": f'${serializer.errors}'}, 400)


    # TODO: 회원 정보 수정
    def put(self, request):
        return Response({'message': 'put method!!'})

    # TODO: 회원 탈퇴
    def delete(self, request):
        return Response({'message': 'delete method!!'})

class UserApiView(APIView):
    # TODO: 로그인 기능
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)