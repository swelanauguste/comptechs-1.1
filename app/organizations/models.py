from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from utils.assets import TimeStampMixin


class Organization(TimeStampMixin):
    """
    Organization model
    """

    name = models.CharField("Organization's name", max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name



