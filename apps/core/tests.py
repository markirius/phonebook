from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_bakery import baker

from apps.contacts.models import Contacts
from apps.core.views import UserListView
from apps.phones.models import Phones

request_factoru = RequestFactory()


class BaseTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.contact = baker.make(Contacts)
        self.phone = baker.make(
                Phones,
                contact=self.contact,
                phone_number="+558299999999"
            )
        self.phone2 = baker.make(Phones, contact=self.contact)

        self.client.force_login(self.user)


class CoreTest(BaseTest):
    def test_search_user(self):
        request = request_factoru.get(
                reverse("users_search"),
                {"q": self.user.username}
            )
        view = UserListView()
        view.request = request
        qs = view.get_queryset()
        query = User.objects.filter(username=self.user.username)
        self.assertEqual(str(qs), str(query))

    def test_search_user_none(self):
        request = request_factoru.get(
                reverse("users_search"),
            )
        view = UserListView()
        view.request = request
        qs = view.get_queryset()
        query = User.objects.all()
        self.assertEqual(str(qs), str(query))
