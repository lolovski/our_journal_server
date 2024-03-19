from datetime import timedelta, datetime, date

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from classes.models import Class, Shedule, Day
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, CreateView
from homeworks.models import Homework, Comment
from homeworks.forms import HomeworkForm, CommentForm



# Create your views here.

User = get_user_model()


@cache_page(15)
def index(request):

    template = 'homeworks/index.html'
    title = 'Homeworks'
    text = 'Главная страница'
    try:
        if request.user.class_user_id:
            class_user = request.user.class_user_id
    except:
        class_user = None
    context = {
        'title': title,
        'text': text,
        'class_user': class_user,

    }
    return render(request, template, context)


def classes(request):
    classes = Class.objects.order_by('-name')
    template = 'homeworks/classes.html'
    context = {
        'classes': classes,

    }
    return render(request, template, context)


@cache_page(15)
@login_required
def classes_homeworks(request, pk):
    classes = get_object_or_404(Class, pk=pk)
    days = Day.objects.all()
    homeworks = Homework.objects.filter(class_user=pk).order_by('week')
    shedules = Shedule.objects.filter(class_user=pk)
    start_week = list()
    start_end_week = list()
    for homework in homeworks:
        start_week.append(homework.week)

    start_week = sorted(list(set(start_week)))

    for week in start_week:
        start_end = [week, week + timedelta(days=6)]
        start_end_week.append(start_end)
    if len(start_end_week) > 1:
        last_week = start_end_week.index(start_end_week[-1])
        for week in range(1, 52):
            if start_end_week[last_week][1] + timedelta(days=7 * week) < date(2024, 6, 1):
                start_end = [start_end_week[-1][0] + timedelta(days=(7)), start_end_week[-1][1] + timedelta(days=7)]
                start_end_week.append(start_end)
    else:
        for week in range(-1, 52):
            if datetime.now().date() - timedelta(datetime.now().weekday()) + timedelta(days=7*week) < date(2024, 6, 1):
                start_end_week.append([datetime.now().date() - timedelta(datetime.now().weekday()) + timedelta(days=7*week), datetime.now().date() - timedelta(datetime.now().weekday()) + timedelta(days=6+7*week)])
    paginator = Paginator(start_end_week, 1)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    template = 'homeworks/classes_homeworks.html'
    context = {
        'homeworks': homeworks,
        'classes': classes,
        'shedules': shedules,
        'start_week': start_week,
        'days': days,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@cache_page(15)
@login_required
def homework_detail(request, class_user_id, homework_id):
    template = 'homeworks/homework_detail.html'
    homework = Homework.objects.get(id=homework_id)
    pub_date_start = homework.week
    pub_date_end = homework.week + timedelta(days=6)
    pub_day = homework.lesson.day
    author_posts = Homework.objects.filter(author=homework.author_id).count()
    comments = homework.comments.select_related('author')
    comments_form = CommentForm()
    context = {
        'homework': homework,
        'pub_date_start': pub_date_start,
        'pub_date_end': pub_date_end,
        'pub_day': pub_day,
        'author_posts': author_posts,
        'comments': comments,
        'comments_form': comments_form,
        'homework_id': homework_id,
    }
    return render(request, template, context)





