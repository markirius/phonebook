from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy 

from apps.contacts.models import Contacts


class ContactCreate(CreateView):
    model = Contacts
    fields = ["name"]
    success_url = reverse_lazy("contacts_list")

    def form_valid(self, form):
        form.instance.name = form.instance.name.title()
        return super(ContactCreate, self).form_valid(form)


class ContactList(ListView):
    model = Contacts
    queryset = Contacts.objects.all().order_by("name")
    paginate_by = 50
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
