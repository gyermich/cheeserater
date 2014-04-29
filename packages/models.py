from django.db import models

# Create your models here.
class Package(models.Model):
  name        = models.CharField(maxlength=300)
  version     = models.CharField(maxlength=300,
                                  blank=True)
  home_page   = models.URLField(blank=True)
  summary     = models.TextField()
  description = models.TextField(blank=True)
  keywords    = models.Textfield(blank=True)
  categories  = models.ManyToManyField(Category,
                        related_name="packages")