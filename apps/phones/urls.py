from django.urls import path

from apps.phones.views import PhoneCreate, PhoneDelete, PhoneUpdate

urlpatterns = [
    path("phone_create/<pk>",
         PhoneCreate.as_view(),
         name="phone_create"
         ),
    path("phone_delete/<pk>",
         PhoneDelete.as_view(),
         name="phone_delete"
         ),
    path("phone_update/<pk>",
         PhoneUpdate.as_view(),
         name="phone_update"
         ),
]
