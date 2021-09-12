from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PasswordModeling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    site = models.CharField(max_length=20)
    url_of_site = models.URLField()
    email = models.EmailField(max_length = 254)
    passwords = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.site


    class Meta:
        ordering = ['-created']




