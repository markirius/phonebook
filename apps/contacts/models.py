from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name

    def save(self):
        self.name = self.name.title()
        if Contacts.objects.filter(name=self.name).exists():
            return None
        super(Contacts, self).save()
