from django.urls import path

from apps.contacts.views import (ContactCreate, ContactDelete, ContactList,
                                 ContactUpdate)

urlpatterns = [
    path("contact_create", ContactCreate.as_view(), name="contact_create"),
    path("contact_delete/<pk>",
         ContactDelete.as_view(),
         name="contact_delete"
         ),
    path("contact_update/<pk>",
         ContactUpdate.as_view(),
         name="contact_update"
         ),
    path("", ContactList.as_view(), name="contacts_list"),
    path("change_language",
         ContactList.change_language,
         name="change_language"
         )
]
