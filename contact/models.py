from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.EmailField(default="")
    subject = models.CharField(default="", max_length=50)
    message = models.TextField(default="")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}\' contact ({self.date})'
