from django.db import models

# Create your models here.
class order(models.Model):
    name = models.CharField(max_length=50)
    img =models.ImageField(upload_to='hinhanh')
    desc = models.TextField()
    price = models.IntegerField()
    isd =models.TextField()
    special = models.BooleanField(default=False)


class cart1(models.Model):
    user_name = models.CharField(max_length=50)
    user_address= models.CharField(max_length=60)
    user_price = models.CharField(max_length=50)
    user_product = models.CharField(max_length=50)
    user_file = models.FileField(upload_to='hinhanh')
    user_time = models.DateTimeField(auto_now=True)
    
    