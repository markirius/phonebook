from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("contacts_list")


class UserListView(ListView):
    model = User
    queryset = User.objects.all().order_by("username")
    template_name = "core/user_list"
    context_object_name = "users"
