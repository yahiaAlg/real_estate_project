from django.db import models


class Realtor(models.Model):

    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="realtors/%Y/%M/%d")
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
class Listing(models.Model):

    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms__ = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.FloatField()
    list_date = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to="listings/%Y/%M/%d")
    photo_1 = models.ImageField(upload_to="listings/%Y/%M/%d")
    photo_2 = models.ImageField(upload_to="listings/%Y/%M/%d")
    photo_3 = models.ImageField(upload_to="listings/%Y/%M/%d")
    photo_4 = models.ImageField(upload_to="listings/%Y/%M/%d")
    photo_5 = models.ImageField(upload_to="listings/%Y/%M/%d")
    photo_6 = models.ImageField(upload_to="listings/%Y/%M/%d")

    def __str__(self):
        return self.title
