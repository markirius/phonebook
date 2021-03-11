from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name
