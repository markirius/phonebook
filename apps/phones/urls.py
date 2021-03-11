from django.urls import path

from apps.phones.views import PhoneCreate, PhoneDelete

urlpatterns = [
    path("phone_create/<pk>",
         PhoneCreate.as_view(),
         name="phone_create"
         ),
    path("phone_delete/<pk>",
         PhoneDelete.as_view(),
         name="phone_delete"
         ),
]
