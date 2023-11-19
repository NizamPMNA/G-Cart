from django.db import models

# Create your models here.

class Register(models.Model):
    email = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.email
    