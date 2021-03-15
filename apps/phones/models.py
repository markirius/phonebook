from django.core.validators import RegexValidator
from django.db import models

from apps.contacts.models import Contacts


class Phones(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+9999999999'. \
        Up to 15 digits allowed",
    )
    phone_number = models.CharField(
            validators=[phone_regex],
            max_length=17,
            blank=True
    )
    contact = models.ForeignKey(
            Contacts,
            on_delete=models.CASCADE,
            related_query_name="contact_phone"
    )

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return self.phone_number

    def save(self):
        if Phones.objects.filter(phone_number=self.phone_number).exists():
            return None
        super(Phones, self).save()
