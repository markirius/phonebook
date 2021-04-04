from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker

from apps.phones.models import Phones


class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
                username="driver",
                email="driver@mail.com",
                password="123driver321"
        )

        self.phone = baker.make(Phones, phone_number="+558299999999")


class PhonesTest(BaseTest):
    def test_str_phone_numbers(self):
        phone = Phones.objects.get(pk=1)
        self.assertEquals(phone.__str__(), phone.phone_number)

    def test_empty_number(self):
        self.phone = baker.make(Phones, phone_number="")
        self.assertIsNone(self.phone.pk)

    def test_exist_number(self):
        self.phone = baker.make(Phones, phone_number="+558299999999")
        self.assertIsNone(self.phone.pk)
