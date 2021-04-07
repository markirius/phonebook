from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_bakery import baker

from apps.contacts.models import Contacts
from apps.contacts.views import ContactList

request_factory = RequestFactory()


class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
                username="driver",
                email="driver@mail.com",
                password="123driver321"
        )

        self.contact = baker.make(
                Contacts,
                name="contact_test",
                email="contacttest@mail.com"
            )
        self.client.force_login(self.user)


class ContactsListTest(BaseTest):
    def test_get_queryset(self):
        request = request_factory.get(
                reverse("contacts_search"),
                {"q": self.contact.name}
            )
        view = ContactList()
        view.request = request
        qs = view.get_queryset()
        query = Contacts.objects.filter(name=self.contact.name)
        self.assertEqual(str(qs), str(query))


class ContactsModelTest(BaseTest):
    def test_save_exist_contact(self):
        contact = baker.make(
                Contacts,
                name="contact_test",
                email="contacttest@mail.com"
            )
        self.assertIsInstance(contact, Contacts)
