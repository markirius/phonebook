from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import translation
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.contacts.models import Contacts
from phonebook import settings


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")
    queryset = Contacts.objects.all().order_by("name")


class ContactList(ListView):
    model = Contacts
    paginate_by = 6
    queryset = Contacts.objects.all().order_by("name")
    context_object_name = "contacts"

    def change_language(request):  # TODO: Work on redirects
        response = HttpResponseRedirect('/')
        if request.method == 'POST':
            language = request.POST.get('language')
            if language:
                if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                    redirect_path = f'/{language}/'
                elif language == settings.LANGUAGE_CODE:
                    redirect_path = '/'
                else:
                    return response
                translation.activate(language)
                response = HttpResponseRedirect(redirect_path)
        return response


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_list")


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contacts
    fields = ["name", "email"]
    success_url = reverse_lazy("contacts_list")
