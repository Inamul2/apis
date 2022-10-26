from django.db import models


# Create your models here.
class CustomerData(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.TextField()
    phoneNumber = models.CharField(max_length=20)
    emailAddress = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pinCode = models.IntegerField()

    def __str__(self):
        return self.name
