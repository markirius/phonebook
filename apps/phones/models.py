from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _

from apps.contacts.models import Contacts


class Phones(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=_("Phone number must be entered in the format: '+9999999999'. \
        Up to 15 digits allowed"),
    )
    phone_number = models.CharField(
            verbose_name=_("Phone Number"),
            validators=[phone_regex],
            max_length=17,
            blank=True,
    )
    contact = models.ForeignKey(
            Contacts,
            on_delete=models.CASCADE,
            related_query_name="contact_phone"
    )

    class Meta:
        verbose_name = _("Phone")
        verbose_name_plural = _("Phones")

    def __str__(self):
        return self.phone_number

    def save(self, force_insert=False, using=None):
        if Phones.objects.filter(phone_number=self.phone_number).exists():
            return Phones.objects.none()
        if self.phone_number == "":
            return Phones.objects.none()
        super(Phones, self).save(force_insert, using)
