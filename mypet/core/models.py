from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='media', null=True)
    begin_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
