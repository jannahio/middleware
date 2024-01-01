from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Sites'

    def __str__(self):
        return self.name

# Jannah user model
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatars/%Y/%m/%d/',
        default='users/avatars/default.jpg'
    )
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=100, null=True)
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'

    def __str__(self):
        return self.username

# Boot layer model
class Boot(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'boot'
        verbose_name_plural = '3. Boots'

    def __str__(self):
        return self.name

# Network model
class Network(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'network'
        verbose_name_plural = '4. Networks'

    def __str__(self):
        return self.name

# Storage model
class Storage(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    class Meta:
        verbose_name = 'storage'
        verbose_name_plural = '5. Storages'

    def __str__(self):
        return self.name

# Compute model
class Compute(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    class Meta:
        verbose_name = 'compute'
        verbose_name_plural = '6. Computes'

    def __str__(self):
        return self.name

# UX model
class UX(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    class Meta:
        verbose_name = 'ux'
        verbose_name_plural = '7. UXs'

    def __str__(self):
        return self.name

# Feedback model
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    class Meta:
        verbose_name = 'feedback'
        verbose_name_plural = '8. Feedbackss'

    def __str__(self):
        return self.name

# Workflow model
class Workflow(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    isStarted = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'workflow'
        verbose_name_plural = '9. Workflows'

    def __str__(self):
        return self.name