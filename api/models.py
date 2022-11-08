from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=50, blank=False, default="")
    description = models.CharField(max_length=300, blank=False, default="")
    published = models.BooleanField(default=False)

    def __str__(self):
      return self.title
