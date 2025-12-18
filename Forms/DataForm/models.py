from django.db import models

# Create your models here.
class Contact_form(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=300)
    created_ate=models.DateTimeField(auto_now_add=True)
    models.CharField()

    def __str__(self):
        return self.name
