from django.core.exceptions import ValidationError
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from listUsers.models import ValidUser


class SingUp(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('classes:index')
    template_name = 'users/signup.html'

    def form_valid(self, form, *args, **kwargs):
        first_name = self.request.POST.get('first_name')
        middle_name = self.request.POST.get("middle_name")
        last_name = self.request.POST.get("last_name")
        try:
            if ValidUser.objects.get(first_name=first_name, middle_name=middle_name, last_name=last_name) is not None:
                user = form.save()
                user.status = ValidUser.objects.get(first_name=first_name, middle_name=middle_name, last_name=last_name).status
                user.class_user = ValidUser.objects.get(first_name=first_name, middle_name=middle_name, last_name=last_name).class_user
                return super().form_valid(form)

        except ValidUser.DoesNotExist:
            raise ValidationError("Введите корректное ФИО")




"""# Импортируем CreateView, чтобы создать ему наследника
# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):

    form_class — из какого класса взять форму
    success_url — куда перенаправить пользователя после успешной отправки формы
    template_name — имя шаблона, куда будет передана переменная form с объектом HTML-формы.

    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy("posts:index")
    template_name = "users/signup.html"
"""