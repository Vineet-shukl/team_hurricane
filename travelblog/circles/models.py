from django.db import models
from django.conf import settings

class Circle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_circles'
    )
    password = models.CharField(max_length=50) # For joining, not for hashing
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='joined_circles'
    )

    def __str__(self):
        return self.name