from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.contacts.models import Contacts


class ContactCreate(CreateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")
    queryset = Contacts.objects.all().order_by("name")


class ContactList(ListView):
    model = Contacts
    paginate_by = 6
    queryset = Contacts.objects.all().order_by("name")
    context_object_name = "contacts"


class ContactDelete(DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_list")


class ContactUpdate(UpdateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")
