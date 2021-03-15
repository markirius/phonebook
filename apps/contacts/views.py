from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.contacts.models import Contacts


class ContactCreate(CreateView):
    model = Contacts
    fields = ["name"]
    success_url = reverse_lazy("contacts_list")

    def form_valid(self, form):
        # implement a solution for error messages to unique constraint error
        form.instance.name = form.instance.name.title()
        return super(ContactCreate, self).form_valid(form)


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
    fields = ["name"]
    success_url = reverse_lazy("contacts_list")

    def form_valid(self, form):
        form.instance.name = form.instance.name.title()
        return super(UpdateView, self).form_valid(form)
