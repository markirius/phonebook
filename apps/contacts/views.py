from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.contacts.models import Contacts


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")


class ContactList(ListView):
    model = Contacts
    paginate_by = 6
    queryset = Contacts.objects.all().order_by("name")
    context_object_name = "contacts"


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_list")


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")
