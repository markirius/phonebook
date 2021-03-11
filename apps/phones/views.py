from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.contacts.models import Contacts
from apps.phones.models import Phones


class PhoneCreate(CreateView):
    model = Phones
    fields = ["phone_number"]
    success_url = reverse_lazy("contacts_list")

    def form_valid(self, form):
        contact = Contacts.objects.get(pk=self.kwargs["pk"])
        form.instance.contact = contact
        return super(PhoneCreate, self).form_valid(form)


class PhoneDelete(DeleteView):
    model = Phones
    success_url = reverse_lazy("contacts_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
