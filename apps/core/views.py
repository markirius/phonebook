from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("contacts_list")


class UserListView(LoginRequiredMixin, ListView):
    model = User
    queryset = User.objects.all().order_by("username")
    template_name = "core/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        if self.request.user:
            queryset = User.objects.all().order_by(
                    "username"
                    ).exclude(
                            username=self.request.user
                            )
            return queryset


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users")
    template_name = "core/user_confirm_delete.html"
