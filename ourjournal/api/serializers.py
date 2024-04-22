from datetime import datetime, timedelta

from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from homeworks.models import Homework

from users.models import User, Achievement, AchievementUser

from classes.models import Class, Shedule, Lesson


class SheduleSerializer(serializers.ModelSerializer):
    lesson_name = serializers.CharField(source='lesson.name')
    day_name = serializers.CharField(source='day.name')

    def __init__(self, *args, **kwargs):
        super(SheduleSerializer, self).__init__(*args, **kwargs)

        self.day_name = serializers.CharField(source='day.name')

    class Meta:
        model = Shedule
        fields = ('lesson_name', 'day_name', 'number', 'id')


class AchievementSerializer(ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name',)


class HomeworkSerializer(ModelSerializer):
    # author = serializers.StringRelatedField(read_only=True)
    lesson_detail = SheduleSerializer(required=False, source='lesson')

    class Meta:
        model = Homework
        fields = ('text', 'lesson_detail', 'lesson', 'week', 'author', 'class_user', 'weekday')

    def get_week(self, obj):
        now = datetime.now()
        return now.date() - timedelta(days=now.weekday())

    def get_class_user(self, obj):
        return User.objects.get(username=self.initial_data['author']).class_user

    def create(self, validated_data):
        return Homework.objects.create(**validated_data)



class ListHomeworksSerializer(ModelSerializer):

    class Meta:
        model = Homework
        fields = ('text', 'lesson', 'week', 'author', 'class_user')



class UserSerializer(ModelSerializer):
    homeworks = serializers.StringRelatedField(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'homeworks', 'achievements')

    def create(self, validated_data):
        if 'achievements' not in self.initial_data:
            user = User.objects.create(**validated_data)
            return user
        achievements = validated_data.pop('achievements')

        user = User.objects.create(**validated_data)

        for achievement in achievements:
            current_achievement, status = Achievement.objects.get_or_create(**achievement)
            AchievementUser.objects.create(achievement=current_achievement, user=user)

        return user

    def update(self, instance, validated_data):

        achievements = self.initial_data.pop('achievements')
        for achievement in achievements:
            current_achievement, status = Achievement.objects.get_or_create(**achievement)
            AchievementUser.objects.create(achievement=current_achievement, user=instance)
        return instance


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class TgIdUsersSerializer(ModelSerializer):
    username = serializers.StringRelatedField(required=False)

    class Meta:
        model = User
        fields = ('username', 'tg_id', 'api_token', 'class_user_id', 'id')

"""    def update(self, instance, validated_data):

        tg_id = self.initial_data.pop('tg_id')
        user = User.objects.get(username=self.initial_data.pop('username'))
        user.tg_id = tg_id
        user.save()
        return instance"""