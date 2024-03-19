from datetime import datetime, date, timedelta
from classes.models import Shedule, Day
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, CreateView

from homeworks.forms import HomeworkForm, CommentForm

from homeworks.models import Homework


weekday = {'Понедельник': 0, 'Вторник': 1, 'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5}

# Create your views here.

User = get_user_model()


@login_required
def homework_create(request, lesson_id, week):

    if request.method == 'POST':
        form = HomeworkForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.author = request.user
            homework.class_user = request.user.class_user
            homework.lesson_id = lesson_id
            homework.week = datetime.strptime(week, '%d.%m.%Y').date()

            homework.save()
            return redirect(f"/classes/{homework.class_user.id}")

    template = 'homeworks/homework_create.html'
    form = HomeworkForm

    context = {
        'form': form,
        'lesson_id': lesson_id,
        'week': week,
    }
    return render(request, template, context)


@cache_page(15)
@login_required
def profile(request, username):
    template = 'users/profile.html'
    user = User.objects.get(username=username)
    last_name = user.last_name
    first_name = user.first_name
    class_user = user.class_user
    class_user_id = class_user.id
    hw_count = Homework.objects.filter(author=user).count()
    top_class = User.objects.filter(class_user=class_user).order_by('-homeworks')

    for i in range(0, len(top_class)):
        if top_class[i] == top_class.get(username=username):
            top_place_class = i + 1
            break

    context = {
        'username': username,
        'last_name': last_name,
        'first_name': first_name,
        'class_user': class_user,
        'hw_count': hw_count,
        'class_user_id': class_user_id,
        'top_place_class': top_place_class,
    }
    return render(request, template, context)


@login_required
def add_comment(request, homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.homework = homework
        comment.save()
    return redirect('classes:homework_detail', homework_id=homework_id, class_user_id=homework.class_user_id)

"""class HomeworkView(CreateView):

    form_class = HomeworkForm
    template_name = 'homeworks/create_homework.html'
    success_url = reverse_lazy('classes:classes_homeworks')

    homework = Homework.objects.create(class_id=User.Class_id, author_id=User.pk, 

    def form_valid(self, form):
        now_wd = datetime.now().weekday()
        now = datetime.now()
        hw_day = self.request.POST.get('lesson_id')
        day_id = Shedule.objects.get(id=hw_day).day_id
        if weekday.get(Day.objects.get(id=day_id).name) <= now_wd:
            hw = form.save(commit=False)
            hw.week = date(now.year, now.month, now.day - now.weekday()) + timedelta(days=7)
            hw.save()
        else:
            hw = form.save(commit=False)
            hw.week = date(now.year, now.month, now.day - now.weekday())
            hw.save()"""

"""now_wd = datetime.now().weekday()
            now = datetime.now()
            hw_day = lesson_id
            day_id = Shedule.objects.get(pk=hw_day).day_id_id

            if weekday.get(Day.objects.get(pk=day_id).name) <= now_wd:
                homework.week = date(now.year, now.month, now.day - now.weekday()) + timedelta(days=7)
            else:
                homework.week = date(now.year, now.month, now.day - now.weekday())"""


