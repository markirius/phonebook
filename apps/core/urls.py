from django.urls import path

from apps.core.views import (PasswordChangeView, UserCreateView, UserDeleteView,
                             UserListView)

urlpatterns = [
    path("user_create/", UserCreateView.as_view(), name="user_create"),
    path(
        "password_change/",
        PasswordChangeView.as_view(),
        name="password_change"
    ),
    path("users/", UserListView.as_view(), name="users"),
    path("user_delete/<pk>", UserDeleteView.as_view(), name="user_delete"),
    path("users/", UserListView.get_queryset, name="users_search"),
]
