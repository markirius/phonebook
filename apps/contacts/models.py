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

    def save(self):
        self.name = self.name.title()
        if Contacts.objects.filter(name=self.name).exists():
            return None
        super(Contacts, self).save()
