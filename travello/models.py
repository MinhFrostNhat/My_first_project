from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    img =models.ImageField(upload_to='hinhanh')
    desc = models.TextField()
    price = models.IntegerField()
    isd =models.TextField()
    special = models.BooleanField(default=False)