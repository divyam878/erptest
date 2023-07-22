from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    registrationNo = models.CharField(max_length=50)
    verified = models.CharField(max_length=50)
    created = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
