from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from organizations.models import Organization


class User(AbstractUser):
    is_data_entry_clerk = models.BooleanField(default=True)
    is_developer = models.BooleanField(default=False)
    is_ministry_of_health = models.BooleanField(default=False)
    # pass


class Profile(models.Model):
    """
    User Profile model
    """
    GENDER_LIST = [
        ("M", "M"),
        ("F", "F"),
    ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField("date of birth", blank=True, null=True)
    
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    contact = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("users:profile-detail", kwargs={"slug": self.slug})

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        return self.user.username
