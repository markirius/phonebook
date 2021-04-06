from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from apps.contacts.models import Contacts
from apps.phones.models import Phones


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
        self.phone = baker.make(Phones, phone_number="+558299999999")
        self.client.force_login(self.user)


class PhonesTest(BaseTest):
    def test_str_phone_numbers(self):
        phone = Phones.objects.get(pk=1)
        self.assertEqual(phone.__str__(), phone.phone_number)

    def test_empty_number(self):
        self.phone = baker.make(Phones, phone_number="")
        self.assertIsNone(self.phone.pk)

    def test_exist_number(self):
        self.phone = baker.make(Phones, phone_number="+558299999999")
        self.assertIsNone(self.phone.pk)

    def test_form_valid_phonecreate(self):
        data = {
                "phone_number": "+558299999998",
                "contact": self.contact
            }
        response = self.client.post(
                reverse("phone_create", kwargs={"pk": self.contact.pk}),
                data=data
            )
        self.assertEqual(Phones.objects.count(), 2)
        self.assertRedirects(response, "/")

    def test_form_invalid_phonecreate(self):
        data = {
                "phone_number": self.phone.phone_number,
                "contact": self.contact
            }
        response = self.client.post(
                reverse("phone_create", kwargs={"pk": self.contact.pk}),
                data=data
            )
        self.assertEqual(Phones.objects.count(), 1)
        self.assertRedirects(response, "/")

    def test_phone_delete(self):
        response = self.client.get(
                reverse(("phone_delete"), kwargs={"pk": self.phone.pk}),
            )
        self.assertEqual(Phones.objects.count(), 0)
        self.assertRedirects(response, "/")
