from django.urls import path

from apps.core.views import PasswordChangeView, SignUpView, UserListView, UserDeleteView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "password_change/",
        PasswordChangeView.as_view(),
        name="password_change"
    ),
    path("users/", UserListView.as_view(), name="users"),
    path("user_delete/<pk>", UserDeleteView.as_view(), name="user_delete"),
]
