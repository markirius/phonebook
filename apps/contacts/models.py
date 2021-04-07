from django.db import models
from django.utils.translation import gettext as _


class Contacts(models.Model):
    name = models.CharField(
            verbose_name=_("Name"),
            max_length=100,
            unique=True
        )
    email = models.EmailField(
            verbose_name=_("Email"),
            max_length=254,
            blank=True
        )

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, using=None):
        self.name = self.name.title()
        self.email = self.email.lower()
        if Contacts.objects.filter(name=self.name).exists() \
                and Contacts.objects.filter(email=self.email).exists():
            return Contacts.objects.none()
        super(Contacts, self).save()
