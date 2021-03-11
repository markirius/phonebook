from django.contrib import admin

from apps.phones.models import Contacts, Phones

admin.site.register(Contacts)
admin.site.register(Phones)
