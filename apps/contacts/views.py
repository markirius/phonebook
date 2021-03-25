from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
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

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Contacts.objects.filter(
                    Q(name__icontains=query) |
                    Q(email__icontains=query) |
                    Q(contact_phone__phone_number__icontains=query)
            )
            return object_list
        return self.queryset


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_list")


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")
