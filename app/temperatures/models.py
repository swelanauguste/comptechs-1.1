from django.db import models
from utils.assets import TimeStampMixin
from django.utils.text import slugify
from django.urls import reverse


class District(TimeStampMixin):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(District, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Temperature(TimeStampMixin):
    """
    Temperature Model
    """

    GENDER_LIST = [
        ("M", "M"),
        ("F", "F"),
    ]
    temp = models.FloatField("temperature", default=0.0)
    name = models.CharField(max_length=200, null=True)
    nic_no = models.CharField("NIC", max_length=8)
    dob = models.DateField("DOB")
    gender = models.CharField(max_length=1, choices=GENDER_LIST, null=True, blank=True)
    address = models.CharField(max_length=100, help_text="Derriere Fort, the Morne")
    district = models.ForeignKey(
        District, related_name="districts", on_delete=models.SET_NULL, null=True
    )
    phone = models.CharField(max_length=20, default="758-")
    email = models.EmailField(blank=True)

    def get_temp_alert(self):
        if self.temp > 37.5:
            return "danger"
        return "success"

    def get_address(self):
        return f"{self.address}, {self.district.name}"

    def get_absolute_url(self):
        return reverse("temperatures:temperature-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("-temp",)

    def __str__(self):
        return f"{self.temp}"
