from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse, path
from django.views.decorators.cache import cache_page
from classes.models import Class, Shedule, Day, Lesson
from core.decorators import school_admin_required
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from classes.forms import ClassForm, SheduleSchoolForm
from school_admin_panel.forms import ClassListForm

from listUsers.models import ValidUser
from listUsers.forms import SchoolUserForm

from users.models import Status




@school_admin_required
@cache_page(15)
def index(request):
    template = 'school_admin/index.html'
    school = request.user.class_user.school.id

    context = {
        "school": school,

    }
    return render(request, template, context)


"""@school_admin_required
@cache_page(15)
def add_class(request):
    if request.method == 'POST':
        form = ClassListForm(request.POST, request.FILES)
        if form.is_valid():
            class_name = form.cleaned_data['class_name']
            new_class = Class.objects.create(name=class_name, school=request.user.class_user.school)
            reverse('school_admin_panel:add_class_list', Class.objects.filter(school=request.user.class_user.school).order_by('-pk')[0].pk + 1, form.cleaned_data['count_students'])
            return HttpResponseRedirect(path)

    template = 'school_admin/add_class.html'
    form = ClassListForm(request.POST or None, request.FILES or None)  # user=request.user

    context = {
        'form': form,

    }
    return render(request, template, context
                  )"""


class AddClass(CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_school_admin'] = self.request.user.is_school_admin()

        return context

    def form_valid(self, form, *args, **kwargs):
        new_class = form.save()
        new_class.school = self.request.user.class_user.school

        return super().form_valid(form)

    template_name = 'school_admin/add_class.html'
    form_class = ClassForm
    success_url = reverse_lazy('school_admin_panel:index')


@school_admin_required
@cache_page(15)
def classes_list(request):
    """if request.method == 'POST':
        form = ClassListForm(request.POST, request.FILES or None, prefix='more')
        if form.is_valid():
            class_name = form.cleaned_data['class_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data['middle_name']
            first_name = form.cleaned_data['first_name']
            school = request.user.class_user.school.id
            status = Status.odject.get(name='ученик').id
            class_user = int(class_id)
            new_user = ValidUser.objects.create(
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                class_user=class_user,
                school=school,
                status=status
            )"""
    template = 'school_admin/classes_list.html'
    school_class_list = Class.objects.filter(school=request.user.class_user.school).order_by('count_students')

    context = {
        'school_class_list': school_class_list
    }
    return render(request, template, context)


@school_admin_required
@cache_page(15)
def add_class_students(request, class_id, count_student):

    if request.method == 'POST':
        form = []
        for i in range(count_student):
            form.append(SchoolUserForm(request.POST or None, request.FILES or None, prefix=i))
        for i in range(len(form)):
            if form[i].is_valid() and form[i].prefix == i:
                new_user = form[i].save(commit=False)
                new_user.school = request.user.class_user.school
                new_user.status = Status.objects.get(name='ученик')
                new_user.class_user_id = class_id
                new_user.save()
        return redirect('school_admin_panel:index')
    template = 'school_admin/add_class_students.html'
    form = []
    for i in range(count_student):
        form.append(SchoolUserForm(request.POST or None, request.FILES or None, prefix=i))
    context = {
        'form': (x for x in form),
        'count_student': count_student,
        'class_id': class_id,
    }
    return render(request, template, context)


@school_admin_required
@cache_page(15)
def add_shedule(request, class_id):
    if request.method == 'POST':
        form = []
        for i in range(1, 51):
            form.append(SheduleSchoolForm(request.POST or None, request.FILES or None, prefix=i))
        for i in range(0, 50):
            try:
                if form[i].is_valid() and form[i].prefix == i + 1 and form[i].data.get('number') != 0 and form[i].data.get('lesson') != 'clean':
                    new_lesson = form[i].save(commit=False)
                    new_lesson.class_user_id = class_id
                    new_lesson.day_id = i // 10 + 1
                    new_lesson.save()
            except:
                ...
        return redirect('school_admin_panel:index')
    template = 'school_admin/add_shedule.html'
    days = []
    for i in range(5):
        days.append(Day.objects.get(pk=i+1))
    form = []
    for i in range(1, 51):
        form.append(SheduleSchoolForm(request.POST or None, request.FILES or None, prefix=i))
    context = {
        'form': (x for x in form),
        'class_id': class_id,
        'days': days,
    }
    return render(request, template, context)


@school_admin_required
@cache_page(15)
def add_student(request, class_id):
    if request.method == 'POST':
        form = SchoolUserForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.class_user_id = class_id
            new_student.school = request.user.class_user.school
            new_student.status = Status.objects.get(name='ученик')
            new_student.save()
            up_class = Class.objects.get(pk=class_id)
            up_class.count_students += 1
            up_class.save()

            return redirect('school_admin_panel:index')

    template = 'school_admin/add_student.html'
    form = SchoolUserForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'class_id': class_id,
    }
    return render(request, template, context)


@school_admin_required
def update_year(request):
    for this_class in Class.objects.filter(school_id=request.user.class_user.school.id):
        if this_class.name[:2] == '11':
            this_class.delete()
    for this_class in Class.objects.filter(school=request.user.class_user.school):
        if 2 < len(this_class.name) < 4:
            this_class.name = str((int(this_class.name[:2]) + 1)) + this_class.name[2]
        elif len(this_class.name) < 3:
            this_class.name = str((int(this_class.name[0]) + 1)) + this_class.name[1]
        this_class.save()
    for shedule in Shedule.objects.all():
        if shedule.class_user.school.id == request.user.class_user.school.id:
            shedule.delete()

    return redirect('school_admin_panel:index')


def update_shedule(request):
    for shedule in Shedule.objects.all():
        if shedule.class_user.school.id == request.user.class_user.school.id:
            shedule.delete()

    return redirect('school_admin_panel:index')


@school_admin_required
def class_delete(request, class_id):
    this_class = Class.objects.get(id=class_id)
    this_class.delete()
    return redirect('school_admin_panel:classes_list')