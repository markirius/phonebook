from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView


class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("contacts_list")


class UserListView(LoginRequiredMixin, ListView):
    model = User
    queryset = User.objects.all().order_by("username")
    paginate_by = 5
    template_name = "core/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = User.objects.filter(
                    Q(username__icontains=query)
            ).order_by("username")
            return object_list
        return self.queryset


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users")
    template_name = "core/user_confirm_delete.html"
