from django.db.migrations import serializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsValidDate
from users.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_list_or_404
from rest_framework import status, generics, viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import HomeworkSerializer, UserSerializer, ListHomeworksSerializer, ClassSerializer, TgIdUsersSerializer, SheduleSerializer
from homeworks.models import Homework
from rest_framework.views import APIView

from classes.models import Class, Day, Shedule, Lesson
from .permissions import IsAuthorOrReadOnly, ReadOnly


class CreateListRetrieveViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class HomeworkViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    lookup_field = 'class_user'

    def get_serializer_class(self):
        #if self.action == 'list':
            #return ListHomeworksSerializer
        return HomeworkSerializer

    def get_queryset(self):
        queryset = Homework.objects.all()
        return queryset

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsValidDate]
            return permission_classes
        permission_classes = [IsAuthenticated]
        return permission_classes

    def retrieve(self, request, *args, **kwargs):

        filters = {}
        for field in self.request.data:

            filters[field] = self.request.data.get(field)
        queryset = Homework.objects.filter(class_user_id=kwargs.get('class_user'), **filters)
        serializer = self.get_serializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TgIdUsersAPI(APIView):

    def get(self, request, format=None):
        try:
            tg_id = self.request.data.get('tg_id')
            user = User.objects.get(tg_id=tg_id)
            serializer = TgIdUsersSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'not registrations': True}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        try:
            user = User.objects.get(username=request.data.get('username'))
            serializer = TgIdUsersSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'DoesNotExist': True}, status=status.HTTP_400_BAD_REQUEST)


class TgSheduleAPI(APIView):

    def get(self, request, format=None):
        try:

            day_name = self.request.data.get('day_name')
            day = Day.objects.get(name=day_name)
            tg_id = self.request.data.get('tg_id')
            user = User.objects.get(tg_id=tg_id)
            class_user = user.class_user.id
            filters = {}
            if self.request.data.get('number') and self.request.data.get('lesson_name') is not None:
                filters['lesson'] = Lesson.objects.get(name=self.request.data.get('lesson_name')).id
                filters['number'] = self.request.data.get('number')

            shedule = Shedule.objects.filter(class_user_id=class_user, day_id=day.id, **filters)
            serializer = SheduleSerializer(shedule, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'not registrations': True}, status=status.HTTP_400_BAD_REQUEST)


"""    def retrieve(self, request, *args, **kwargs):
        try:
            if User.objects.get(tg_id=kwargs.get('tg_id')):
                user = User.objects.get(tg_id=kwargs.get('tg_id'))
                serializer = self.get_serializer(self.get_queryset())
                return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response("Пользователь не зарегистрирован", status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(tg_id=self.request.POST.get('tg_id'))
        return Response(serializer.data, status=status.HTTP_200_OK)

"""



"""    def get_object(self):
    #lookup_fields = ['class_user_id',]
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj"""



"""    def post(self, request, class_user):

        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            new_homework = serializer.save()
            new_homework.class_user_id = class_user
            new_homework.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, class_user):
        homeworks = Homework.objects.filter(class_user=class_user)
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)
"""
